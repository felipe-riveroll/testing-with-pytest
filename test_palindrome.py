""" Test for palindrome.py """

import pytest
from palindrome import is_palindrome


@pytest.mark.parametrize(
    "palindrome",
    [
        "",
        "a",
        "Bob",
        "Never odd or even",
        "Madam, in Eden, I'm Adam",
        "Step on no pets!",
        "Don't nod",
    ],
)
def test_is_palindrome(palindrome):
    """Test for is_palindrome() with valid palindromes"""
    assert is_palindrome(palindrome)


@pytest.mark.parametrize(
    "non_palindrome",
    [
        "abc",
        "abab",
    ],
)
def test_is_not_palindrome(non_palindrome):
    """Test for is_palindrome() with invalid palindromes"""
    assert not is_palindrome(non_palindrome)
