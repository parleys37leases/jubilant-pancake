import re

password = input("🔑 Enter a password: ")
strength = "Weak"
if (len(password) >= 8 and
    re.search(r"\d", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[^\w\s]", password)):
    strength = "Strong"
elif len(password) >= 6:
    strength = "Moderate"

print(f"Password strength: {strength}")
