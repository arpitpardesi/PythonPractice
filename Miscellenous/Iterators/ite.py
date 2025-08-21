it = iter([1,2,3, 4])
print (next(it))
print (it.__next__())
print (it.__next__())
print (next(it))

it = iter([1,2,3, 4, 5])
print (next(it))
while True:
   try:
      no = next(it)
      print (no)
   except StopIteration:
      break

