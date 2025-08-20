from typing import List, TypeVar, Generic

T = TypeVar('T')


class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item


box1 = Box(42)
print(box1.get_item())

box2 = Box('Hello')
print(box2.get_item())
