from algorithm import algorithm
import hashlib

def encoding(password):

    encoded = ""
    for p in password:
        if p in algorithm:
            encoded += algorithm[p]

    encoded224 = hashlib.sha224(encoded.encode()).hexdigest()
    encoded256 = hashlib.sha256(encoded.encode()).hexdigest()
    encoded512 = hashlib.sha512((encoded256 + encoded224).encode()).hexdigest()

    return encoded512


enc = encoding('po2Jbist')
print(enc)
