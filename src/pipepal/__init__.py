"""Main package for pipepal."""
from .app import hello_world

__all__ = ['hello_world']

"""
This is the content of the README.md file.
"""
with open('../../README.md', 'r') as file:
    __doc__ = file.read()