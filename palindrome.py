""" Check if a string is a palindrome. """
import string as s


def is_palindrome(string):
    """Check if a string is a palindrome."""
    string = (
        string.lower()
        .replace(" ", "")
        .translate(str.maketrans("", "", s.punctuation))
    )
    return string == string[::-1]
