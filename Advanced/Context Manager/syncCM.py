import pyautogui


class SyncContextManager:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        print("Acquiring resource... ", self.resource)

        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource... ", self.resource)

        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress exception if any

# Example usage
with SyncContextManager(resource="MyResource") as res:
    print("Using resource...")
