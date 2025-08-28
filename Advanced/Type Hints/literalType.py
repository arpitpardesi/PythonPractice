from typing import Literal

def move(direction: Literal["left", "right", "up", "down"]) -> None:
   print(f"Moving {direction}")

move("left")  # Valid
move("up")    # Valid                                     