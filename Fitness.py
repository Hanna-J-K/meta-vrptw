from Encoding import decode, total_distance
import reader


data = reader.read_file('R101.txt')


def fitness(particle):
    particle.decoded = decode(particle, data)
    return sum([total_distance(truck, data) for truck in particle.decoded])
