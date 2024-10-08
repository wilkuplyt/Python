import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the password length: "))
print("Generated password:", password_generator(length))
