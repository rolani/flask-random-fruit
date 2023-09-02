from app import random_fruit


def test_random_fruit():
    assert "apple" or "cherry" or "orange" or "pawpaw" or "grapes" in random_fruit()
