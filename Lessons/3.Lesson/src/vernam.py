def encode(key, message):
    output = ""
    for i in range(len(message)):
        index_key = i % len(key)
        output += chr(ord(message[i]) ^ ord(key[index_key]))
    return output

def decode(key, message):
    return encode(key, message)

print(decode("key", encode("key", "message")))