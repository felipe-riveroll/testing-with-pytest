""" Test for format_data.py """

import pytest
from format_data import format_data_for_display, format_data_for_excel

@pytest.fixture
def example_people_data():
    """Example people data"""
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayd",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def test_format_data_for_display(example_people_data):
    """Test for format_data_for_display()"""
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayd Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    """Test for format_data_for_excel()"""    
    assert format_data_for_excel(example_people_data) == """given,family,title
    Alfonsa,Ruiz,Senior Software Engineer
    Sayd,Khan,Project Manager
    """
