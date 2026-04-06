import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    password = "".join(random.choice(all_characters) for _ in range(length))
    
    return password