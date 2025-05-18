# Shtim i 0-ve në fund që të ndahet në grupe nga 6
def to_binary_string(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def base64_encode(text):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary = to_binary_string(text)

    while len(binary) % 6 != 0:
        binary += '0'

    encoded = ''

# dekodimi i nje stringu Base64 ne tekst normal, pa perdorur klasa dhe funksione te gatshme
def base64_decode(encoded_text):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    clean_text = encoded_text.rstrip('=')

    binary = ''
    for char in clean_text:
        index = base64_chars.index(char)
        binary += f'{index:06b}'

    decoded = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) < 8:
            break
        decoded += chr(int(byte, 2))

    return decoded

   # Menu për përdoruesin
   print("Zgjidh një veprim:")
   print("1. Enkripto në Base64")
   print("2. Dekripto nga Base64")
   choice = input("Zgjedhja jote (1/2): ")

   if choice == '1':
       text = input("Shkruaj tekstin që dëshiron të enkriptohet: ")
       encoded = base64_encode(text)
       print("Teksti i enkriptuar:", encoded)

   elif choice == '2':
       encoded_text = input("Shkruaj tekstin e enkriptuar me Base64: ")
       decoded = base64_decode(encoded_text)
       print("Teksti i dekriptuar:", decoded)

   else:
       print("Zgjedhje e pavlefshme.")