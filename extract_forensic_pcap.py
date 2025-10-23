#!/usr/bin/env python3
"""
extract_forensic_pcap.py

Usage:
  python extract_forensic_pcap.py capture.pcapng output_dir [--filter FILTER] [--tshark TSHARK_PATH]

What it does:
- Finds tshark (or uses provided path).
- Computes SHA256 of original pcap.
- Filters the pcap (using the provided FILTER) and writes filtered.pcapng in output_dir.
- Computes SHA256 of filtered pcap.
- Extracts fields (frame.number, frame.time_epoch, ip.src, ip.dst, udp.srcport, udp.dstport, data.data)
  from the filtered pcap and tries to decode data.data as UTF-8 JSON.
- Saves valid JSON payloads to output_dir/json/frame_<frame>_<epoch>.json
- Produces index.csv and manifest.csv (filename, size, sha256, mtime_utc, source_frame)
"""

import os
import sys
import subprocess
import shutil
import csv
import binascii
import hashlib
import datetime
import argparse
import binascii
import csv as _csv
import openpyxl
from openpyxl import Workbook

DEFAULT_TSHARK_PATHS = [
    r"C:\Program Files\Wireshark\tshark.exe",
    r"C:\Program Files (x86)\Wireshark\tshark.exe",
    "/usr/bin/tshark",
    "/usr/local/bin/tshark",
    "/snap/bin/tshark"
]

def extract_payloads(tsv_path):

    with open(tsv_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        parts = line.strip().split("\t")
        if len(parts) < 7 or not parts[6]:
            continue

        frame, epoch, src, dst, sport, dport, hex_payload = parts
        # Converte da HEX a testo ASCII
        # Rimuove tutti i caratteri non esadecimali (es. ':', spazi)
        clean_hex = ''.join(c for c in hex_payload if c in "0123456789abcdefABCDEF")
        # Decodifica in ASCII
        ascii_data = binascii.unhexlify(clean_hex).decode('utf-8', errors='ignore').strip()

def find_tshark(provided=None):
    if provided:
        if os.path.isfile(provided):
            return provided
        # try to expand ~
        p = os.path.expanduser(provided)
        if os.path.isfile(p):
            return p
        print(f"Provided tshark path not found: {provided}")
        return None
    # try which
    tshark = shutil.which("tshark")
    if tshark:
        return tshark
    for p in DEFAULT_TSHARK_PATHS:
        if os.path.isfile(p):
            return p
    return None

def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(8192)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def iso_utc_from_epoch(epoch_str):
    try:
        epoch = float(epoch_str)
        return datetime.datetime.utcfromtimestamp(epoch).replace(microsecond=0).isoformat() + "Z"
    except:
        return ""

def hex_to_bytes(h):
    if not h:
        return b''
    clean = ''.join(c for c in h if c in "0123456789abcdefABCDEF")
    if len(clean) % 2 != 0:
        clean = "0" + clean
    return bytes.fromhex(clean)

# ...existing code...
def run_tshark_extract(tshark, pcap_in, tshark_filter, out_tshark_tsv):
    # request several possible data fields (different Wireshark versions / dissectors)
    fields = [
        "frame.number",
        "frame.time_epoch",
        "ip.src",
        "ip.dst",
        "udp.srcport",
        "udp.dstport",
        "data.data"
    ]
    cmd = [tshark, "-r", pcap_in]
    if tshark_filter:
        cmd += ["-Y", tshark_filter]
    cmd += ["-T", "fields"]
    for f in fields:
        cmd += ["-e", f]
    # include header for easier debugging
    cmd += ["-E", "header=y", "-E", "separator=\\t", "-E", "quote=d"]
    # run and capture stdout to file
    with open(out_tshark_tsv, "w", encoding="utf-8") as outf:
        proc = subprocess.Popen(cmd, stdout=outf, stderr=subprocess.PIPE, text=True)
        _, stderr = proc.communicate()
        if proc.returncode not in (0, 1):  # allow 1 for warnings
            raise RuntimeError(f"tshark failed: {stderr.strip()}")
    return out_tshark_tsv
# ...existing code...

def write_manifest(manifest_path, entries):
    # entries: list of tuples (filename, size_bytes, sha256, mtime_iso, source_frame)
    with open(manifest_path, "w", newline="", encoding="utf-8") as mf:
        w = csv.writer(mf)
        w.writerow(["filename","size_bytes","sha256","mtime_utc","source_frame"])
        for e in entries:
            w.writerow(e)

def main():
    parser = argparse.ArgumentParser(description="Extract payloads from pcap (forensic), compute hashes and manifest.")
    parser.add_argument("pcap", help="Input pcapng/pcap file")
    parser.add_argument("outdir", help="Output directory (will be created)")
    parser.add_argument("--filter", "-f", default="udp.port==4210", help="tshark display filter (default: udp.port==4210)")
    parser.add_argument("--tshark", "-t", default=None, help="Path to tshark executable (optional)")
    parser.add_argument("--keep-tsv", action="store_true", help="Keep intermediate tshark TSV output")
    args = parser.parse_args()

    pcap = args.pcap
    outdir = args.outdir
    tshark_filter = args.filter
    provided_tshark = args.tshark

    if not os.path.isfile(pcap):
        print("Input pcap not found:", pcap)
        sys.exit(1)

    os.makedirs(outdir, exist_ok=True)

    tshark = find_tshark(provided_tshark)
    if not tshark:
        print("tshark not found. Install Wireshark or provide --tshark path.")
        sys.exit(1)
    print("Using tshark:", tshark)

    # 1) compute sha256 original pcap
    sha_orig = sha256_of_file(pcap)
    size_orig = os.path.getsize(pcap)
    print(f"Original pcap: {pcap} size={size_orig} sha256={sha_orig}")

    # 2) produce filtered pcap by using tshark -w (preferably)
    filtered_pcap = os.path.join(outdir, "filtered.pcapng")
    # We will call tshark to write filtered pcap: tshark -r input -Y FILTER -w filtered.pcapng
    cmd_filter = [tshark, "-r", pcap, "-Y", tshark_filter, "-w", filtered_pcap]
    print("Filtering with:", " ".join(cmd_filter))
    proc = subprocess.Popen(cmd_filter, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate()
    if proc.returncode != 0:
        print("Error filtering pcap:", err)
        sys.exit(1)
    if not os.path.isfile(filtered_pcap):
        print("Filtered pcap not created. Exiting.")
        sys.exit(1)
    sha_filtered = sha256_of_file(filtered_pcap)
    size_filtered = os.path.getsize(filtered_pcap)
    print(f"Filtered pcap: {filtered_pcap} size={size_filtered} sha256={sha_filtered}")

    # 3) extract desired fields from filtered pcap to TSV using run_tshark_extract
    tsv_path = os.path.join(outdir, "tshark_extracted.tsv")
    run_tshark_extract(tshark, filtered_pcap, None, tsv_path)  # already filtered pcap -> no extra filter

   # ...existing code...
    # 4) parse TSV and save hex payloads, build index rows

    index_rows = []  # (frame, epoch_ts, ip_src, ip_dst, udp_sport, udp_dport, json_filename)
    manifest_entries = []  # (filename, size_bytes, sha256, mtime_iso, source_frame)
    payload_rows = []  # (hex_payload, size_bytes, sha256, mtime_iso, source_frame)
    
    # open TSV with csv.reader to handle quotes correctly
    with open(tsv_path, "r", encoding="utf-8", errors="ignore") as tsvf:
        reader = _csv.reader(tsvf, delimiter="\t", quotechar='"')
        try:
            header = next(reader)
        except StopIteration:
            header = []
        # normalize header names
        hdr_lower = [h.strip().lower() if h is not None else "" for h in header]
        print("tshark output columns:", header)

        # heuristics to find useful column indexes
        def find_col(possible_names):
            for name in possible_names:
                for i, h in enumerate(hdr_lower):
                    if h == name:
                        return i
            return None

        frame_idx = find_col(["frame.number", "no.", "no", "frame"]) or 0
        time_idx = find_col(["frame.time_epoch", "time_epoch", "time"]) or 1
        src_idx = find_col(["ip.src", "src"]) or 2
        dst_idx = find_col(["ip.dst", "dst"]) or 3
        sport_idx = find_col(["udp.srcport", "udp.srcport"]) or 4
        dport_idx = find_col(["udp.dstport", "udp.dstport"]) or 5

        # find payload/data column: prefer exact names, else first column containing 'data'
        payload_idx = find_col(["data.data"])
        if payload_idx is None:
            for i, h in enumerate(hdr_lower):
                if "data" in h:
                    payload_idx = i
                    break
        if payload_idx is None:
            payload_idx = len(header) - 1 if header else 6

    # re-open to iterate all rows from start (skip header)
    with open(tsv_path, "r", encoding="utf-8", errors="ignore") as tsvf:
        reader = _csv.reader(tsvf, delimiter="\t", quotechar='"')
        try:
            next(reader)  # skip header
        except StopIteration:
            pass

        for i, parts in enumerate(reader, start=1):
            # ensure parts is list
            if not isinstance(parts, list):
                continue

            # safe-get helper
            def get_at(idx):
                return parts[idx].strip() if idx < len(parts) and parts[idx] is not None else ""

            frame_no = get_at(frame_idx)
            epoch_ts = get_at(time_idx)
            ip_src = get_at(src_idx)
            ip_dst = get_at(dst_idx)
            udp_sport = get_at(sport_idx)
            udp_dport = get_at(dport_idx)

            # pick payload from payload_idx; fallback to last column
            hex_payload = get_at(payload_idx) 
            if not hex_payload:
                continue

            # Save raw hex candidate for inspection (one .hex per frame)
            hex_fname= f"frame_{frame_no}.hex"
            hex_path = os.path.join(hex_fname)
            try:
                with open(hex_path, "w", encoding="utf-8") as hf:
                    hf.write(hex_payload if hex_payload is not None else "")
            except Exception:
                pass

            payload_bytes = hex_to_bytes(hex_payload)
            if not payload_bytes:
                continue
            payload_sha = hashlib.sha256(payload_bytes).hexdigest()
            index_rows.append((frame_no, epoch_ts, ip_src, ip_dst, udp_sport, udp_dport))
            payload_rows.append((hex_payload, payload_sha))

    # write index.csv
    index_csv = os.path.join(outdir, "index.csv")
    with open(index_csv, "w", newline="", encoding="utf-8") as idxf:
        w = csv.writer(idxf)
        w.writerow(["frame","time_epoch","ip_src","ip_dst","udp_src","udp_dst","payload_hex","payload_path"])
        for r in index_rows:
            w.writerow(r)

# finire di scrivere payload.csv
    payload_csv = os.path.join(outdir, "payload.csv")
    with open(payload_csv, "w", newline="", encoding="utf-8") as paycsv:
        payloadwrite = csv.writer(paycsv)
        payloadwrite.writerow(["frame","time_epoch","ip_src","ip_dst","udp_src","udp_dst", "payload","payload_sha",])
        for rows in payload_rows:
            payloadwrite.writerow(rows)

    # 5) Build manifest entries: original pcap, filtered pcap, and each json file
    # original pcap
    mtime_orig = datetime.datetime.utcfromtimestamp(os.path.getmtime(pcap)).replace(microsecond=0).isoformat() + "Z"
    manifest_entries.append((os.path.basename(pcap), size_orig, sha_orig, mtime_orig, "original_capture"))

    # filtered pcap
    mtime_f = datetime.datetime.utcfromtimestamp(os.path.getmtime(filtered_pcap)).replace(microsecond=0).isoformat() + "Z"
    manifest_entries.append((os.path.basename(filtered_pcap), size_filtered, sha_filtered, mtime_f, "filtered_capture"))

    #sha index_csv
    sha_index = sha256_of_file(index_csv)
    size_index = os.path.getsize(index_csv)

    #sha payload_csv
    sha_pay = sha256_of_file(payload_csv)
    size_pay = os.path.getsize(payload_csv)

    mtime_indexcsv = datetime.datetime.utcfromtimestamp(os.path.getmtime(index_csv)).replace(microsecond=0).isoformat() + "Z"
    manifest_entries.append((os.path.basename(index_csv), size_index, sha_index, mtime_indexcsv, "index_csv"))

    mtime_paycsv = datetime.datetime.utcfromtimestamp(os.path.getmtime(payload_csv)).replace(microsecond=0).isoformat() + "Z"
    manifest_entries.append((os.path.basename(payload_csv), size_pay, sha_pay, mtime_paycsv, "payloads_csv"))


    wb= Workbook()
    ws_idx= wb.active
    ws_idx.title= "Frames Index"
    ws_idx.append(["frame","time_epoch","ip_src","ip_dst","udp_src","udp_dst","payload_hex"])
    for r in index_rows:
        ws_idx.append(r)

    wb= Workbook()
    ws_idx= wb.active
    ws_idx.title= "Payloads"
    ws_idx.append(["frame","time_epoch","ip_src","ip_dst","udp_src","udp_dst","payload_hex", "payload_sha"])
    for r in index_rows:
        ws_idx.append(r)

    # optional: remove TSV if not requested
    if not args.keep_tsv:
        try:
            os.remove(tsv_path)
        except:
            pass



    # final summary print
    print("=== SUMMARY ===")
    print("Original pcap:", pcap)
    print("Original sha256:", sha_orig)
    print("Filtered pcap:", filtered_pcap)
    print("Filtered sha256:", sha_filtered)
    print("Hex payload saved to:", payload_xlsx)
    print("Manifest:", manifest_xlsx)
    print("Index:", frames_index_xlsx)
    print("If desired, mount a VeraCrypt volume and copy the folder", outdir, "inside it. Then compute SHA256 of the container and store alongside manifest for chain of custody.")
    print("Done.")

if __name__ == "__main__":
    main()
#passare da csv a openpyxl per excel

# cmd command: python extract_forensic_pcap.py iotforensica.pcapng output_dir --filter " ip.src==192.168.0.188" --tshark "C:\Program Files\Wireshark\tshark.exe" 