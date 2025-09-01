from memory_profiler import profile

@profile
def memory_intensive_function():
    # Simulate a memory-intensive operation
    large_list = [i for i in range(1000000)]
    return sum(large_list)

if __name__ == '__main__':
    result = memory_intensive_function()
    print(f"Result: {result}")