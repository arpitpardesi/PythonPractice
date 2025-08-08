# Similar to switch case

def evenOdd(a):
    match a % 2:
        case 0:
            return "EVEN"
        case 1:
            return "Odd"
        case _:
            return "NAN"
# a = int(input())

print(evenOdd(5))
print(evenOdd(4))