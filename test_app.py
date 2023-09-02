"""Random_fruit function from main app"""
from app import random_fruit


def test_random_fruit():
    """Tests random fruit function"""
    assert "apple" or "cherry" or "orange" or "pawpaw" or "grapes" in random_fruit()
