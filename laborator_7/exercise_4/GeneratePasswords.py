import random
import string


def generate_password(length=8, special_chars=True, contains_num=True, contains_upper_case=True):
    characters = string.ascii_letters
    if special_chars:
        characters += string.punctuation

    if contains_num:
        characters += string.digits

    if contains_upper_case:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
