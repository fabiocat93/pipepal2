"""Tests for the app hello_world function."""
from pipepal import hello_world

def test_hello_world(capsys):  # capsys is a built-in fixture provided by pytest to capture stdout and stderr
    hello_world()
    captured = capsys.readouterr()  # Captures the output of hello_world()
    assert "Hello World!\n" == captured.out
