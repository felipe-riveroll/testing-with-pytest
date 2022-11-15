""" test_assert_examples.py """


def test_uppercase():
    """ Test that uppercase() returns a string """
    assert 'loud noises'.upper() == 'LOUD NOISES'


def test_reversed():
    """ Test that reversed() returns a reversed sequence """
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    """ Test that some_primes() check if 37 is a prime number """
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
