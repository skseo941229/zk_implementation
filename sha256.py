import hashlib

string="Home"
encoded=string.encode()
result = hashlib.sha256(encoded)

print("String : ", end ="")

print(string)

print("Hexadecimal same: ",result.hexdigest())
