import tracemalloc

tracemalloc.start()

# our code here
a = 10
b = 20
c = a + b
# Take a snapshot of current memory usage
snapshot = tracemalloc.take_snapshot()

# Display the top 10 memory-consuming lines
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)
