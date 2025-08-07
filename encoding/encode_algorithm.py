from algorithm import algorithm

def encoding(password):

    encoded = ""
    for p in password:
        for letter in algorithm:
            if letter == p:
                encoded += algorithm.get(letter)

    return encoded
