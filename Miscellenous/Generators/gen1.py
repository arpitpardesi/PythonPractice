def count(max):
    c = 0
    while c < max:
        yield c
        c += 1
co = count(10)
for i in co:
    print(i)

while True:
    try:
        print(next(co))
    except StopIteration:
        break

gen_expr = (x * x for x in range(1, 6))

for value in gen_expr:
    print(value)