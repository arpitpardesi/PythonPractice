a = {1,2,3,4,5,6,7,8,9,10}

for i in a:
    print(i, end = " ")

set = iter(a)
while True:
    try:
        print(next(set), end=" ")
    except StopIteration:
        break
print('\n')
for i,j in enumerate(a):
    print(i, end=" ")

    