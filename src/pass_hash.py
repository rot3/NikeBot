import hashlib
import random
import string
SALT = 'TwmjfEIyGS0o8MB'

def hash_password(password):
    return hashlib.sha256((SALT + password).encode()).hexdigest()
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)

