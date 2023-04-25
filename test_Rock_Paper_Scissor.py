import builtins

from rock_paper_scissor import win, required
from io import StringIO
from unittest.mock import patch
import pytest

def main():
    test_win()

def test_win():
    assert win(2, 2, 1) == False
    assert win(4, 2, 4) == False
    assert win(2, 1, 0) == True

def test_required(monkeypatch):
    required.__setattr__(builtins.input, lambda _: "Mark")
    i = input()
    assert i == "Mark"


if __name__ == '__main__':
    main()
