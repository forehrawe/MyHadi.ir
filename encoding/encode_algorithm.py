from algorithm import algorithm
import hashlib

def encoding(password):

    encoded = ""
    for p in password:
        for letter in algorithm:
            if letter == p:
                encoded += algorithm.get(letter)
                
    encoded = hashlib.sha256(encoded.encode()).hexdigest()
    encoded = hashlib.sha512(encoded.encode()).hexdigest()

    return encoded


enc = encoding('po2Jbist')
print(enc)
