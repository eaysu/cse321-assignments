def max_antennas(antennas):
    # sort antennas based on their rightmost coverage point
    sorted_antennas = sorted(antennas, key=lambda x: x[1])

    # initialize variables
    activated_antennas = []
    current_rightmost = float('-inf')

    # greedy algorithm to activate antennas
    for antenna in sorted_antennas:
        if antenna[0] > current_rightmost:
            # activate the antenna if it doesn't intersect with existing activated antennas
            activated_antennas.append(antenna)
            current_rightmost = antenna[1]

    return activated_antennas

# test usage
antennas = [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]
result = max_antennas(antennas)
print(f"The maximum number of activated antennas is: {len(result)}")
print(f"Activated antennas: {result}")
