from typing import Optional

def divide(a: float, b: float) -> Optional[float]:
   if b == 0:
      return None
   else:
      return a / b

result1: Optional[float] = divide(10.0, 2.0)   # result1 will be 5.0
result2: Optional[float] = divide(10.0, 0.0)   # result2 will be None

print(result1)
print(result2)                                           