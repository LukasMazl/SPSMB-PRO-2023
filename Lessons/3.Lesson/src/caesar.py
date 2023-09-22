def encode(key, message):
    output = ""
    for character in message:
        output += chr(ord(character) + key)
    return output

def decode(key, message):
    return encode(-key, message)


print(encode(1, "Ahoj"))