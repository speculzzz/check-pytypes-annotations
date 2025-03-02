"""
TODO:

foo only accepts literal 'left' and 'right' as its argument.
"""
from typing import Literal

T = Literal['left','right']

def foo(direction: T):
    pass


foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
foo(a)  # expect-type-error
