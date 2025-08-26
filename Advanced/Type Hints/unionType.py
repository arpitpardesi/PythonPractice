from typing import Union

def square_root_or_none(number: Union[int, float]) -> Union[float, None]:
   if number >= 0:
      return number ** 0.5
   else:
      return None

result1: Union[float, None] = square_root_or_none(50)
result2: Union[float, None] = square_root_or_none(-50)

print(result1)
print(result2)