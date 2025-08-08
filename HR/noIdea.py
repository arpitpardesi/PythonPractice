n, m = map(int, input().split(" "))
print(n, m)
nL = input().split(" ")
print(nL)
A = input().split(" ")
print(A)
B = input().split(" ")
print(B)

h = 0

for i in nL:
    if i in A:
        h += 1
    if i in B:
        h += -1

print(h)
