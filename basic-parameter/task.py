"""
TODO:

foo can accept an integer argument, None or no argument at all.
"""

def foo(x: int):
    pass


foo(10)

foo("10") #expect-type-error
