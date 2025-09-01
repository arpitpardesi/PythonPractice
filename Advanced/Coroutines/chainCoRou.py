def producer(sentence, next_coroutine):
   '''
   Splits the input sentence into tokens and sends them to the next coroutine.
   '''
   tokens = sentence.split(" ")
   for token in tokens:
      next_coroutine.send(token)
   next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
   '''
   Filters tokens based on the specified pattern and sends matching tokens to the next coroutine.
   '''
   print(f"Searching for {pattern}")
   try:
      while True:
         token = (yield)
         if pattern in token:
            next_coroutine.send(token)
   except GeneratorExit:
      print("Done with filtering!!")
      next_coroutine.close()

def print_token():
   '''
   Receives tokens and prints them.
   '''
   print("I'm the sink, I'll print tokens")
   try:
      while True:
         token = (yield)
         print(token)
   except GeneratorExit:
      print("Done with printing!")

# Setting up the pipeline
pt = print_token()
pt.__next__()

pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Tutorialspoint is welcoming you to learn and succeed in Career!!!"
producer(sentence, pf)