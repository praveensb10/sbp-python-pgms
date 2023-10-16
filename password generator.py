import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_check(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in '!@#$%^&*()' for char in password):
        return False
    return True

def generate_secure_password(length=8):
    while True:
        password = generate_password(length)
        if password_check(password):
            return password

print(generate_secure_password())