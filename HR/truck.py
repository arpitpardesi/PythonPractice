"""
Suppose there is a circle. There are N petrol pumps on that circle.
Petrol pumps are numbered 0 to (N - 1) (both inclusive). You have two pieces of information corresponding to each of the petrol pump:
(1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.
Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
"""

def tour(petrol, distance):
    n = len(petrol)
    start = 0
    end = 0
    current_petrol = 0

    while start < n:
        current_petrol += petrol[end] - distance[end]

        if current_petrol < 0:
            start = end + 1
            end = start
            current_petrol = 0
        else:
            end += 1

        if end == n:
            return start

    return -1  # If no solution exists

# Example usage
petrol = [4, 6, 7, 4]
distance = [6, 5, 3, 5]
result = tour(petrol, distance)
if result != -1:
    print(f"The truck can start at petrol pump {result}.")
else:
    print("The truck cannot complete the tour from any petrol pump.")
