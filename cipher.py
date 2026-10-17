text = b"<some text to encrypt>"

key = b"adm"

result = [text[i] ^ key[i % len(key)] for i in range(len(text))]

with open("result.txt", "w") as f:
    f.write(str(result))
