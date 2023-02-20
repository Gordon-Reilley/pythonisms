from pythonisms import Pythonisms
import pytest
from pythonisms import Pythonisms


def test_len():
    pun = ["I dont trust stairs...", "they're always up to something "]
    assert len(pun) == 2


def test_iter():
    pun = ["I dont trust stairs...", "they're always up to something "]
    iterator = iter(pun)
    assert next(iterator) == "I dont trust stairs..."
    assert next(iterator) == "they're always up to something "


def test_get_item():
    p = Pythonisms([1, 2, 3])
    assert p[0] == 1
    assert p[1] == 2
    assert p[2] == 3

def test_set_item():
    p = Pythonisms([1, 2, 3])
    p[2] = 4
    assert p[2] == 4
    assert p.data == [1, 2, 4]