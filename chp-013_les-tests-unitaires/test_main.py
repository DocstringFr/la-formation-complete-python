import pytest

from main import add


def test_add_with_two_numbers():
    assert add(5, 10) == 15


def test_add_with_two_letters():
    assert add("a", "b") == "ab"


def test_add_with_two_booleans():
    assert add(True, False) == 0
    assert add(True, True) == 2
    assert add(False, False) == 0


def test_add_with_two_none():
    with pytest.raises(TypeError):
        add(None, None)
