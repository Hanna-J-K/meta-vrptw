from Particle import Particle
from Encoding import *
import reader

if __name__ == "__main__":
    particle = Particle(200)
    data = reader.read_file('R101.txt')
    decoded = decode(particle, data)
    all = sum([total_distance(truck, data)
              for truck in decode(particle, data)])
    print(all)
