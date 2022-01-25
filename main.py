from Particle import Particle
from Encoding import *
import reader

if __name__ == "__main__":
    # particle = Particle(200)
    # data = reader.read_file('R101.txt')
    # decoded = decode(particle, data)
    # all = sum([total_distance(truck, data)
    #           for truck in decode(particle, data)])
    # print(all)
    vehicles = [[64, 65, 70, 78], [46, 47, 48], [40, 42, 90, 93], [21, 72, 73], [31, 63, 69, 89], [20, 22, 55, 66], [36, 91], [5, 81, 88, 98], [15, 58, 84], [33, 34, 75], [4, 12, 82, 95], [6, 18, 35, 59], [51], [39, 60, 94, 96], [76], [28], [
        16, 41, 43, 85], [27], [1, 56], [19, 50], [3, 37, 74], [11, 25], [26], [86], [10, 17, 61], [24, 38, 54], [8, 57, 62, 87], [32, 67, 68], [0, 9], [29, 49, 77], [2, 23, 53, 79, 80], [92, 97], [7, 13, 45, 99], [14, 71], [52], [30, 44, 83]]
    new_vehicles = list(map(lambda x: list(map(lambda y: y + 1, x)), vehicles))
    # thehicles = [[41, 91, 95], [1, 93, 94], [5, 44, 81], [11, 26, 75], [17, 59, 82], [34, 70, 80], [0, 2, 32, 78], [28, 67, 76, 79], [20, 72, 74], [7, 18, 19, 46], [6, 48, 61, 62], [13, 37, 43, 56], [
    #     12, 36, 84, 92], [9, 10, 63, 69], [33, 64, 65, 77], [15, 42, 85, 97], [27, 30, 87], [14, 39, 71, 86], [31, 51, 68, 89], [3, 55, 73], [58, 90, 96, 98], [8, 29, 49, 50], [21, 22, 25, 54], [4, 16, 60, 83], [23, 52, 53], [24, 38, 40, 66]]
    # x = sum([total_distance(truck, data) for truck in vehicles])
    distances = [total_distance(truck, data) for truck in new_vehicles]
    print(distances)
    y = sum(distances)
    # z = sum([total_distance(truck, data) for truck in thehicles])
    # print(x)
    print(y)
    # print(z)
    pass
