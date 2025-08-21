def A(a):
    def B(b, c):
        return a + b + c

    return B


closure = A(5)
res = closure(12, 5)
print(res)
