import random
import string


def generate_password(length):
    if length < 6:  # Ensures a minimum of security
        print("The password must be at least 6 characters long.")
        return None

    # Set of possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    new_password = ''.join(random.choice(characters) for i in range(length))
    return new_password


# Example of use
desired_length = 12  # You can modify this value
password = generate_password(desired_length)
print("Password generated:", password)
