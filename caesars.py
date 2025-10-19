def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    mode = input("Type 'encrypt' to encode or 'decrypt' to decode: ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    output = caesar_cipher(text, shift, mode)
    print(f"Result: {output}")