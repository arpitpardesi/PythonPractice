import asyncio


class AsyncContextManager:
    def __init__(self, resource):
        self.resource = resource

    async def __aenter__(self):
        print("Acquiring resource... ", self.resource)

        return self.resource
    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Releasing resource... ", self.resource)

        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True
# Suppress exception if any
# Example usage
async def main():
    async with AsyncContextManager(resource="abcd") as resource:
        print("Using resource...")

asyncio.run(main())