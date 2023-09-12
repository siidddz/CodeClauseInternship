import string
import random
def generate_password(length, hint):
    """Generate a random password of a given length and hint."""
    # The password will be composed of printable ascii characters
    chars = string.ascii_letters + string.digits
    # Generate a random password of the given length
    password = ''.join(random.choice(chars) for i in range(length))
    # If the user wants their name in the password, add it
    if hint == "name":
        password = password + hint
    return password
# Example
length = int(input("How long do you want your password to be? "))
hint = input("What do you want as a hint? ")
password = generate_password(length, hint)
print(password)
