def add(a):
    def add_inner(b):
        return a + b
    return add_inner

closure = add(5)
res = closure(12)
print(res)