from Encoding import decode, total_distance, encode


def fitness(particle):
    particle.decoded = decode(particle.position)
    particle.position = encode(particle)
    return sum([total_distance(truck) for truck in particle.decoded])
