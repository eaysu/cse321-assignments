# drone class definition
class Drone:
    # every drone have x and y coordiantes
    def __init__(self, x, y):
        self.x = x
        self.y = y

# function to calculate the distance between two drones
def distance(drone1, drone2):
    return ((drone1.x - drone2.x) ** 2 + (drone1.y - drone2.y) ** 2) ** 0.5

# divide-and-conquer algorithm to find the minimum distance between any pair of drones
def min_distance_drones(drones):
    # if the number of drones is small (3 or less), use a brute-force approach
    if len(drones) <= 3:
        return min(distance(drones[i], drones[j]) for i in range(len(drones)) for j in range(i + 1, len(drones)))

    # sort drones based on their x-coordinate to divide 2 halves
    sorted_drones = sorted(drones, key=lambda drone: drone.x)

    # divide the set of drones into two halves
    mid = len(sorted_drones) // 2
    left_half = sorted_drones[:mid]
    right_half = sorted_drones[mid:]

    # recursively find the minimum distance in each half
    min_left = min_distance_drones(left_half)
    min_right = min_distance_drones(right_half)

    # find the minimum distance between points on the left and right halves
    min_lr = min(min_left, min_right)

    # create a strip containing points within the minimum distance from the middle line
    strip = [drone for drone in sorted_drones if abs(drone.x - sorted_drones[mid].x) < min_lr]

    # sort the strip based on y-coordinate
    strip.sort(key=lambda drone: drone.y)

    # check for the minimum distance within the strip
    min_strip = min(distance(strip[i], strip[j]) for i in range(len(strip)) for j in range(i + 1, min(7, len(strip))))

    # return the global minimum distance
    return min(min_lr, min_strip)

# test usage
drones = [Drone(1, 2), Drone(5, 6), Drone(8, 3), Drone(12, 9), Drone(4, 11)]
min_dist = min_distance_drones(drones)
print(f"The minimum distance between any pair of drones is: {min_dist}")
