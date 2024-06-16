import re


def password_strength(password):
    length = len(password)

    #criteria
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[\W_]', password) is not None

    # Strength score
    score = 0

    #points based on criteria
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    #Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    #Feedback
    feedback = []
    if length < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Password should include at least one uppercase letter.")
    if not has_lower:
        feedback.append("Password should include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should include at least one digit.")
    if not has_special:
        feedback.append("Password should include at least one special character.")

    return strength, feedback


def main():
    while True:
        password = input("Enter your password (or type 'exit' to quit): \n ")
        if password.lower() == 'exit':
            break
        strength, feedback = password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print("Feedback:")
        if feedback:
            for f in feedback:
                print(f"- {f}")
        else:
            print("Your password is strong!")
        print("\n")


if __name__ == "__main__":
    main()