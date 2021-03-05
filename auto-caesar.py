from hashlib import sha512
file = input('Enter the path of the file : ')
key = sha512(input('Enter the key : ').encode('utf-8')).digest()
with open(file, 'rb') as f_input:
    i = 0
    b = bytes()
    while f_input.peek():
        b += bytes([ord(f_input.read(1))^key[i%len(key)]])
with open(file, 'wb') as f_output:
    f_output.write(b)