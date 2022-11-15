""" Fixture example test_fixture_demo.py """

import pytest


@pytest.fixture
def example_fixture():
    """This is a fixture"""
    return 1


def test_with_fixture(example_fixture):
    """This test uses the fixture"""
    assert example_fixture == 1
