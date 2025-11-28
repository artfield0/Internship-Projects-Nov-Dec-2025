import re

def check_password_strength(password):
    score = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "special_chars": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    # Count how many criteria met
    score = sum(criteria.values())

    if score <= 2:
        level = "Weak"
    elif score == 3:
        level = "Medium"
    elif score == 4:
        level = "Strong"
    else:
        level = "Very Strong"

    return score, level, criteria


if __name__ == "__main__":
    pwd = input("Enter a password to test strength: ")
    score, level, criteria = check_password_strength(pwd)

    print("\nPassword Strength Results:")
    for key, value in criteria.items():
        print(f"{key.capitalize()}: {'✔️ Passed' if value else '❌ Failed'}")

    print(f"\nOverall Strength: {level} ({score}/5)")
