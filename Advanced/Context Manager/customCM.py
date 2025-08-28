import asyncio
from contextlib import asynccontextmanager, contextmanager

@contextmanager
def my_context_manager():
   print("Entering the context manager method")
   try:
      yield
   finally:
      print("Exiting the context manager method")

with my_context_manager():
   print("Inside the context")

print("--------------------------------")

@asynccontextmanager
async def async_context_manager():
   try:
      print("Entering the async context")
      # Perform async setup tasks if needed
      yield
   finally:
      # Perform async cleanup tasks if needed
      print("Exiting the async context")

async def main():
   async with async_context_manager():
      print("Inside the async context")
      await asyncio.sleep(1)  # Simulating an async operation

# Run the asyncio event loop
asyncio.run(main())