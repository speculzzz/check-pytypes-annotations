"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""
import typing

T = typing.TypeVar("T", bound="Foo")

class Foo:
    def return_self(self) -> T:
        pass


class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()

sf: SubclassOfFoo = Foo().return_self() # expect-type-error
