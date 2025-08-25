import weakref

class Myclass:
   def __del__(self):
      print('(Deleting {})'.format(self))
obj = Myclass()
r = weakref.ref(obj)

print('object:', obj)
print('reference:', r)
print('call r():', r())

print('deleting obj')
del obj
print('r():', r())