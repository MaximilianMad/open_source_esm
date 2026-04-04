""" --- Unit tests for password strength utility functions. --- """

import unittest
from utils import (
    check_length,
    check_character_types,
    calculate_strength,
    generate_feedback,
)


class TestPasswordUtils(unittest.TestCase):
    """Test cases for password strength functions."""

    def test_check_length_valid(self):
        """Password of sufficient length should return True."""
        self.assertTrue(check_length("Password123"))

    def test_check_length_invalid(self):
        """Password shorter than 8 characters should return False."""
        self.assertFalse(check_length("Password123"))

    def test_check_character_types(self):
        """Function should detect character categories correctly."""
        result = check_character_types("Abc123!")
        self.assertEqual(result, (True, True, True, True))

    def test_calculate_strength(self):
        """Strength score should match expected scoring logic."""
        score = calculate_strength("Abc123!")
        self.assertEqual(score, 4)

    def test_generate_feedback_strong(self):
        """Strong password should return 'Strong' with no suggestions."""
        strength, suggestions = generate_feedback("Abc123!xyz")
        self.assertEqual(strength, "Strong")
        self.assertEqual(suggestions, [])

    def test_generate_feedback_weak(self):
        """Weak password should return suggestions."""
        strength, suggestions = generate_feedback("abc")
        self.assertEqual(strength, "Weak")
        self.assertTrue(len(suggestions) > 0)


if __name__ == "__main__":
    unittest.main()
