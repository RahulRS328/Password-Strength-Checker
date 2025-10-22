import requests
import hashlib

def analyze_password(password):
    """Analyze password strength and return a score"""
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        remarks.append("Add numbers.")

    if any(c in "!@#$%^&*()_+-=[]{}|;':,./<>?" for c in password):
        score += 1
    else:
        remarks.append("Add special characters.")

    return {"score": score, "remarks": remarks}

def suggest_stronger_password(password):
    """Generate a simple stronger password suggestion"""
    suggestion = password

    if len(password) < 8:
        suggestion += "123!"
    if not any(c.isupper() for c in password):
        suggestion = suggestion.capitalize()
    if not any(c.isdigit() for c in password):
        suggestion += "9"
    if not any(c in "!@#$%^&*()_+-=[]{}|;':,./<>?" for c in password):
        suggestion += "!"

    return suggestion

def check_pwned(password):
    """Check if password is found in known data breaches"""
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1pwd[:5], sha1pwd[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True
    return False
