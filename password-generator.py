import random
import string

def leet_transform(text):
    leet_map = {
        'a': '@',
        'A': '@',
        'e': '3',
        'E': '3',
        'i': '1',
        'I': '1',
        'o': '0',
        'O': '0',
        's': '$',
        'S': '$',
        't': '7',
        'T': '7'
    }
    return ''.join(leet_map.get(c, c) for c in text)

def generate_password_from_name(full_name, total_length=16):
    names = full_name.strip().split()
    if len(names) != 2:
        return "Please enter exactly two names (e.g., 'John Doe')."

    first, last = names

    # Leet-transform the first 3 characters of the first name and preserve position
    prefix = leet_transform(first[:3])

    # Take last 3 chars of last name, leet-transform them
    suffix = leet_transform(last[-3:])

    # Add 3 random digits
    digits = ''.join(random.choices(string.digits, k=3))

    # Alternate special characters
    specials = ''.join(['.' if i % 2 == 0 else '?' for i in range(2)])

    # Random filler to meet desired length
    filler_len = total_length - (len(prefix) + len(suffix) + len(digits) + len(specials))
    filler = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=filler_len))

    # Combine without shuffling the prefix
    password = prefix + suffix + digits + specials + filler
    return password

# --- User interaction ---
full_name = input("Enter your first and last name (e.g., John Doe): ")
try:
    strong_password = generate_password_from_name(full_name)
    print("Generated Secure Password:", strong_password)
except Exception as e:
    print("Error:", e)
