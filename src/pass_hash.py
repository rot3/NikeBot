import hashlib
import random
import string
#SALT = 'TwmjfEIyGS0o8MB'

def hash_str(word,salt):
    return hashlib.sha256((salt + word).encode()).hexdigest()

def get_random_salt(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

