# try:
#     res = 10 / 0
# except ZeroDivisionError as e:
#     print(e)
#     raise RuntimeError from e


try:
   open("nofile.txt")
except OSError:
   raise RuntimeError("unable to handle error")