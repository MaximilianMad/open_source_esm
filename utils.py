""" ---- Functions for the Password Strength Analyser ----"""

def check_length(password):
    """Check if the password length is sufficient."""
    return len(password) >= 8


def check_character_types(password):
    """Check for presence of lowercase, uppercase, digits, and symbols."""
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    return has_lower, has_upper, has_digit, has_symbol


def calculate_strength(password):
    """Calculate password strength score."""
    score = 0

    if check_length(password):
        score += 1

    char_types = check_character_types(password)
    score += sum(char_types)  # add 1 point per type present

    return score


def generate_feedback(password):
    """Generate a strength label and suggestions."""
    score = calculate_strength(password)
    has_lower, has_upper, has_digit, has_symbol = check_character_types(password)

    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not has_lower:
        suggestions.append("Add lowercase letters.")
    if not has_upper:
        suggestions.append("Add uppercase letters.")
    if not has_digit:
        suggestions.append("Add numbers.")
    if not has_symbol:
        suggestions.append("Add symbols (e.g., !@#$).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions
