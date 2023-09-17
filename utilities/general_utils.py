import random
import string


def generate_random_email(base_email):
    # Create random string
    random_chars = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(10))

    # Insert random string in the base email
    random_gmail = f"{base_email.split('@')[0]}+{random_chars}@{base_email.split('@')[1]}"

    return random_gmail

