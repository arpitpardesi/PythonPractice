a = [1,5,8,4,2,7,8,9,3,6,0,2,4,5,7,8,9,10]

def e(s):
    return s % 2 == 0

a.sort(key=e, reverse=False)
print(a)