import tkinter as tk
from tkinter import ttk
def verifycell():
    x=x_var.get()
    y=y_var.get()
    #Zona 1: Nord America
    if(x==1):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dagli Stati Uniti d'America o dal Canada")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1242):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Bahamas")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1246):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Barbados")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1264):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Anguille, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1268):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Antigua e Barbuda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1284):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Vergini Britanniche, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1340):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Vergini Americane, Territorio degli Stati Uniti D'America")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1345):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Cayman, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1441):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Bermuda, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1473):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Grenada")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1649):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Turks e Caicos, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1658 or x==1876):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Giamaica")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1664):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Montserrat, Territorio Brittanico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1670):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Marianne Settentrionali, Territorio degli Stati Uniti d'America")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1671):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Guam, Territorio degli Stati Uniti d'America")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1684):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Samoa Americane, Territorio degli Stati Uniti d'America")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1721):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Sint Maarten")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1758):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Saint Lucia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1767):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Dominica")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1784):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Saint Vicent e Grenadine")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1787 or x==1939):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Puerto Rico, Territorio degli Stati Uniti d'America")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1809 or x==1829 or x==1849):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Repubblica Dominicana")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1868):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Trinidad e Tobago")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==1869):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Saints Kittens e Nevis")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 2: Africa
    if(x==20):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Egitto")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==210):
        z_label=ttk.Label(frame, text="Prefisso non attivo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==211):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Sud Sudan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==212):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Marocco")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==213):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Algeria'")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==214 or x==215):
        z_label=ttk.Label(frame, text="Prefisso non attivo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==216):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Tunisia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==217):
        z_label=ttk.Label(frame, text="Prefisso non attivo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==218):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Libia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==219):
        print(f"Prefisso non attivo")
        z_label=ttk.Label(frame, text="Prefisso non attivo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==220):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Gambia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==221):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Senegal")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==222):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Mauritania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==223):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Mali")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==224):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Guinea")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==225):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Costa d'Avorio")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==226):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Burkina Faso")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==227):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Niger")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==228):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Togo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==229):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Benin")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==230):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Mauritius")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==231):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Liberia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==232):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Sierra Leone")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==233):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Ghana")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==234):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Nigeria")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==235):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Ciad")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==236):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Repubblica Centrafricana")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==237):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Camerun")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==238):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Capo Verde")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==239):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da São Tomé e Principe")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==240):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Guinea Equatoriale")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==241):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Gabon")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==242):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Repubblica del Congo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==243):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Repubblica Democratica del Congo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==244):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Angola")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==245):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Guinea-Bissau")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==246):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Isola di Diego Garcia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==247):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Isola Ascensione,Territorio Britannico d'Oltremare di Ascensione, Sant'Elena e Tristan da Cunha")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==248):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Seychelles")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==249):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Sudan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==250):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Ruanda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==251):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Etiopia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==252):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Somalia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==253):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Gibuti")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==254):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Kenya")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==255):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Tanzania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==256):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Uganda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==257):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Burundi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==258):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Mozambico")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==259):
        z_label=ttk.Label(frame, text="Prefisso non attivo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==260):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dallo Zambia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==261):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Madagascar")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==262):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Riunione e Mayotte, dipartimenti e regioni d'oltremare francesi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==263):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dallo Zimbabwe")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==264):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Namibia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==265):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Malawi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==266):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Lesotho")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==267):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Botswana")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==268):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'eSwatini")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==269):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Comore")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==27):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Sudafrica")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==290):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Sant'Elena o Tristan da Cunha, Territorio Britannico d'Oltremare di Ascensione, Sant'Elena e Tristan da Cunha")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==291):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Eritrea")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==295):
        z_label=ttk.Label(frame, text="Il prefisso corretto per San Marino è +378")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==297):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Aruba, regno dei Paesi Bassi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==298):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Fær Øer, regno di Danimarca")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==299):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Groenlandia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 3: Europa pt.1
    if(x==30):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Grecia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==31):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dai Paesi Bassi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==32):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Belgio")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==33):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Francia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==34):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Spagna")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==350):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Gibilterra, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==351):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Portogallo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==352):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Lussemburgo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==353):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Irlanda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==354):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Islanda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==355):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Albania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==356):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Malta")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==357):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Cipro")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==358):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Finlandia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==359):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Bulgaria")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==36):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Ungheria")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==37):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Lituania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==371):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Lettonia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==372):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Estonia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==373):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Moldavia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==374):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Armenia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==375):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Bielorussia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==376):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Andorra")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==377):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Principato di Monaco")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==378):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da San Marino")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==379):
        z_label=ttk.Label(frame, text="Ex Stato Città del Vaticano, usa il prefisso della città di Roma +39 06698")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==380):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Ucraina")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==381):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Serbia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==382):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Montenegro")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==383):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Kosovo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==385):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Croazia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==386):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Slovenia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==387):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Bosnia-Erzegovina")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==388):
        z_label=ttk.Label(frame, text="Non più in uso, ex Spazio di numerazione telefonica europeo - Servizi Europei")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==389):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Macedonia del Nord")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==39):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Italia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 4 Europa pt.2
    if(x==40):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Romania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==41):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Svizzera")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==420):
        print(f"Il numero +{x} {y} proviene dalla Cechia, ex Repubblica Ceca")
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Cechia, ex Repubblica Ceca")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==421):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Slovacchia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==423):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Liechtenstein")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==43):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Austria")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==44):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Regno Unito")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==45):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Danimarca")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==46):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Svezia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==47):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Norvegia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==48):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Polonia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==49):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Germania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 5 CentroAmerica, SudAmerica ed Indie Occidentali
    if(x==500):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Falkland, Territorio Britannico d'Oltremare")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==501):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Belize")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==502):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Guatemale")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==503):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da El Salvador")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==504):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Honduras")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==505):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Nicaragua")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==506):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Costa Rica")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==507):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Panama")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==508):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Saint Pierre et Miquelon")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==509):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Haiti")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==51):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Peru")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==52):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Messico")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==53):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Cuba")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==54):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Argentina")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==55):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Brasile")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==56):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Cile")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==57):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Colombia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==58):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Venezuela")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==590):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Guadalupa")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==591):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Bolivia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==592):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Guyana")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==593):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Ecuador")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==594):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Guyana Francese, dipartimenti e regioni d'oltremare francesi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==595):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Paraguay")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==596):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Martinica")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==597):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Suriname")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==598):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Uruguay")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5993):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Sint Eustasius")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5994):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Saba")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5995):
        z_label=ttk.Label(frame, text="Ex prefisso di Sint Marteen, ora +1721")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5997):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Bonaire")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5998):
        z_label=ttk.Label(frame, text="Ex prefisso di Aruba, ora +297")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==5999):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Curaçao")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 6: Pacifico Meridionale ed Oceania
    if(x==60):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Malaysia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==61):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Australia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==62):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Indonesia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==63):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Filippine")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==64):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Nuova Zelanda")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==65):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Singapore")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==66):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Thailandia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==670):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Timor Est")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==671):
        z_label=ttk.Label(frame, text="Ex prefisso di Guam, ora +1671")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==672):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dai Territori Australi Esterni")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==673):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Brunei")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==674):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Nauru")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==675):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Papua Nuova Guinea")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==676):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Tonga")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==677):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Salomone")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==678):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Vanuatu")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==679):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Figi")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==680):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Palau")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==681):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Wallis e Futuna")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==682):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Cook")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==683):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Niue")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==684):
        z_label=ttk.Label(frame, text="Ex prefisso delle Samoa Americane, ora +1684")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==685):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Samoa")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==686):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Kiribati o Isole Gilbert")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==687):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Nuova Caledonia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==688):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Tuvalu o dalle Isole Elice")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==689):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Polinesia Francese")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==690):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Tokelau")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==691):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dagli Stati Federati di Micronesia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==692):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Isole Marshall")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 7: Russia
    if(x==7):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Russia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 8: Asia Orientale e servizi speciali
    if(x==800):
        z_label=ttk.Label(frame, text="Il numero è usato dall'International Freephone")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==808):
        z_label=ttk.Label(frame, text=f"Il numero è riservato agli Shared Cost Services o viene dall'Isola di Wake")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==81):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Giappone")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==82):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Corea del Sud")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==84):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Vietnam")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==850):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Corea del Nord")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==852):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Hong Kong")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==853):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Macao")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==855):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Cambogia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==856):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Laos")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==86):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Cina")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==870):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Servizio Inmarsat 'SNAC'")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==871 or x==872 or x==873 or x==874):
        z_label=ttk.Label(frame, text="Dismessi, ex suddivisione di Inmarsat ora +870")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==875 or x==876 or x==877 or x==879):
        z_label=ttk.Label(frame, text="Servizio Mobile Marittimo")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==878):
        z_label=ttk.Label(frame, text="Universal Personal Telecommunications Services")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==880):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Bangladesh")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==881):
        z_label=ttk.Label(frame, text="MObile Satellite System")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==882 or x==883):
        z_label=ttk.Label(frame, text="International Networks")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==886):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Taiwan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==888):
        z_label=ttk.Label(frame, text="Ufficio Nazioni Unite per Affari Umanitari, OCHA")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    #Zona 9: Asia occidentale e meridionale, Medio Oriente
    if(x==90):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Turchia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==91):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'India")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==92):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Pakistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==93):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Afghanistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==94):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dallo Sri Lanka")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==95):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Birmania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==960):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalle Maldive")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==961):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Libano")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==962):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Giordania")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==963):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Siria")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==964):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Iraq")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==965):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Kuwait")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==966):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Arabia Saudita")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==967):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dallo Yemen")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==968):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Oman")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==969):
        z_label=ttk.Label(frame, text="Ex Repubblica Democratica dello Yemen, ora +967")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==970):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dallo Stato di Palestina")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==971):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dagli Emirati Arabi Uniti")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==972):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene da Israele")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==973):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Bahrein")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==974):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Qatar")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==975):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Bhutan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==976):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Mongolia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==977):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Nepal")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==978):
        z_label=ttk.Label(frame, text="Dismesso, ex Dubai ora +971")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==979):
        z_label=ttk.Label(frame, text="International Premium Rate Service, ex Abu Dhani ora +971")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==98):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Iran")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==991):
        z_label=ttk.Label(frame, text="International Telecommunications Public Correspondence Service Trial (ITPCS)")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==992):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Tagikistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==993):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Turkmenistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==994):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dall'Azerbaigian")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==995):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dalla Georgia")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==996):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Kirghizistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==997):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Kazakistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)
    if(x==998):
        z_label=ttk.Label(frame, text=f"Il numero +{x} {y} proviene dal Uzbekistan")
        z_label.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        calculate_button=ttk.Button(frame, text="Termina", command=root.destroy)
        calculate_button.grid(column=1, row=6, padx=5, pady=20, sticky=tk.EW)

root=tk.Tk()
root.title("Verifica prefisso telefonico")
root.geometry("600x400+400+180")
x_var=tk.IntVar()
y_var=tk.IntVar()
z_var=tk.StringVar()
frame=ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW)
x_label=ttk.Label(frame, text="Prefisso")
x_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
x_entry=ttk.Entry(frame, textvariable=x_var)
x_entry.grid(column=3, row=0,sticky=tk.EW, padx=5, pady=5)
y_label=ttk.Label(frame, text="Numero di telefono")
y_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
y_entry=ttk.Entry(frame, textvariable=y_var)
y_entry.grid(column=3, row=1,sticky=tk.EW, padx=5, pady=5)
calculate_button=ttk.Button(frame, text="Verifica", command=verifycell, default='active')
calculate_button.grid(column=1, row=3, padx=5, pady=20, sticky=tk.EW)
chart_frame=ttk.Frame(root)
chart_frame.grid(column=1,row=0,sticky=tk.NSEW)
root.mainloop()