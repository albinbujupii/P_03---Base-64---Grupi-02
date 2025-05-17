
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