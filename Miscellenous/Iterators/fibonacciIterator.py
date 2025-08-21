class Fibo:
    def __init__(self, max):
        self.max = max
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration

        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

f = Fibo(100)
for i in f:
    print(i)

