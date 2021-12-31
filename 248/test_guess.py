from unittest.mock import patch, MagicMock
from collections import deque

import pytest

from guess import GuessGame, InvalidNumber, MAX_NUMBER

# write test code to reach 100% coverage and a 100% mutpy score

def test_invalid_secret_numbers():
    with pytest.raises(InvalidNumber, match='Not a number'):
        GuessGame('haha')
    with pytest.raises(InvalidNumber, match='Negative number'):
        GuessGame(-50)
    with pytest.raises(InvalidNumber, match='Number too high'):
        GuessGame(MAX_NUMBER+50)
    with pytest.raises(InvalidNumber, match='Number too high'):
        GuessGame(MAX_NUMBER+1)

def test_valid_secret_numbers(monkeypatch, capsys):
    g = GuessGame(9)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 9)
        g()
        captured = capsys.readouterr()
        assert "Guess a number: " in captured.out
        assert "You guessed it!\n" in captured.out


def test_valid_max_number(monkeypatch, capsys):
    g = GuessGame(15)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 15)
        g()
        captured = capsys.readouterr()
        assert "Guess a number: " in captured.out
        assert "You guessed it!\n" in captured.out

def test_valid_secret_numbers(monkeypatch, capsys):
    g = GuessGame(0)
    assert g.attempt == 0
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 0)
        g()
        captured = capsys.readouterr()
        assert "You guessed it!\n" in captured.out


def make_multiple_inputs(inputs):
    def next_input():
        return inputs.popleft()
    return next_input


def test_invalid_guess(capsys, monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(deque(["a", 9])))
    g = GuessGame(9)
    g()
    captured = capsys.readouterr()
    assert g.attempt == 1
    assert "Enter a number, try again\n" in captured.out
    assert "You guessed it!\n" in captured.out
    

def test_too_low(monkeypatch, capsys):
    g = GuessGame(9)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 5)
        g()
        captured = capsys.readouterr()
        assert "Too low\n" in captured.out

def test_too_high(monkeypatch, capsys):
    g = GuessGame(9)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 12)
        g()
        captured = capsys.readouterr()
        assert "Too high\n" in captured.out

def test_max_guesses(monkeypatch, capsys):
    g = GuessGame(9)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        captured = capsys.readouterr()
        assert f"Sorry, the number was 9\n" in captured.out
        assert g.max_guesses == 5


def test_max_guesses_2(monkeypatch, capsys):
    g = GuessGame(9, 8)
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        m.setattr('builtins.input', lambda: 12)
        g()
        captured = capsys.readouterr()
        assert f"Sorry, the number was 9\n" in captured.out
        assert g.max_guesses == 8
    
def test_max_number():
    assert MAX_NUMBER == 15

