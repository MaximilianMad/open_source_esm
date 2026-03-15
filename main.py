""" ---- Main Program for the Password Strength Analyser ---- """
from utils import generate_feedback

password = input("Enter a password to analyze: ")

strength, suggestions = generate_feedback(password)

print("\nPassword strength:", strength)

if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print("-", s)
else:
    print("Good password!")
