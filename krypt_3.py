key = [6,9,4,2,0]
msg = input("Enter a message to encrypt: ")
encmsg = ""

z = 0
#y = 0

for ch in msg:
    if z < len(key):
        asc = ord(ch) + key[z]
    else:
        z = 0
        asc = ord(ch) + key[z]
    ench = chr(asc)
    encmsg += ench
    z = z + 1
print("Encrypted message:",encmsg)
