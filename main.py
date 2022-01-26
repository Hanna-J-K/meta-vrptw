from Particle import Particle
from Encoding import *

if __name__ == "__main__":
    particle = Particle(200)
    decode(particle)
    vehicles = [[84, 74, 80], [2, 35, 70], [88, 37, 100], [77, 78, 24, 54, 39], [89, 96, 58, 51], [97, 93, 38], [69, 1, 10, 59], [26, 79, 25], [72, 85, 16, 48], [95, 98, 18, 4], [6, 91, 43, 82], [13, 42, 73, 56], [29, 66, 32], [30, 49, 60], [
        71, 3, 50], [76, 68, 34, 31], [52, 7, 8, 46, 17], [57, 23, 55], [27, 99, 94], [53, 40, 63], [90, 20], [5, 86], [36, 19], [47, 64], [28, 41], [62, 81], [45, 61, 87], [12, 22], [21], [83, 44], [15], [67], [9], [65], [33], [75], [11], [14], [92]]
    print(sum([total_distance(truck) for truck in vehicles]))
    pass
