# Enums in Python

from enum import Enum

class subjects(Enum):
    MATH = 1
    SCIENCE = 2
    HISTORY = 3
    GEOGRAPHY = 4

obj =  subjects.MATH
print(obj)  # Output: subjects.MATH
print(obj.name)  # Output: MATH
print(obj.value)  # Output: 1

for subject in subjects:
    print(subject.name, subject.value)