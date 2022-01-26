from Encoding import decode, total_distance


def fitness(particle):
    particle.decoded = decode(particle.position)
    return sum([total_distance(truck) for truck in particle.decoded])
