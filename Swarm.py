import numpy as np
from Fitness import fitness
import Particle
import matplotlib.pyplot as plt
import random
from Crossbreed import crossover, mutate
import Encoding
from Params import DATA
import reader

POPULATION = 200
ITERATIONS = 100


def generate_swarm():
    return [Particle.Particle() for _ in range(POPULATION)]


def find_minimum(swarm):
    crossover_probability = 0.2
    mutation_probability = 0.01
    global_best_adaptation = np.inf
    global_best_position = None
    best_positions = []
    best_adaptations = []
    for _ in range(ITERATIONS):
        for particle in swarm:
            particle.find_best_adaptation()
            particle.calculate_new_velocity()
            particle.move_to_new_position()

            if particle.best_adaptation < global_best_adaptation:
                global_best_adaptation = particle.best_adaptation
                global_best_position = particle.position

            if random.random() <= crossover_probability:
                old_position = particle.position.copy()
                particle.position = crossover(
                    particle.position, global_best_position)
                if fitness(particle) < particle.adaptation:
                    particle.position = old_position

            if random.random() <= mutation_probability:
                particle.position = mutate(particle.position)
        best_adaptations.append(global_best_adaptation)
        best_positions.append(global_best_position)

    return best_positions, best_adaptations


def refresh_data(name, capacity):
    global DATA
    FILENAME = name
    DATA = reader.read_file(FILENAME)
    DISTANCES = reader.distance_array(FILENAME).tolist()

    Encoding.DISTANCES = DISTANCES
    Encoding.DATA = DATA
    Encoding.CAPACITY = capacity

    Particle.CAPACITY = capacity


def draw_swarm(name, capacity):
    refresh_data(name, capacity)
    print(name)
    swarm = generate_swarm()
    best_positions, best_adaptations = find_minimum(swarm)
    trucks = Encoding.decode(best_positions[-1])
    print(len(trucks), best_adaptations[-1])
    print(trucks)
    plt.figure()
    plt.plot(np.arange(ITERATIONS), best_adaptations)
    plt.title(name)
    plt.savefig(f"plots/swarm/{name}.png")

    plt.figure()
    paths_x = [[DATA[customer][0] for customer in [0] + truck + [0]]
               for truck in trucks]
    paths_y = [[DATA[customer][1] for customer in [0] + truck + [0]]
               for truck in trucks]
    for x, y in zip(paths_x, paths_y):
        plt.plot(x, y, '--', linewidth=0.5)
        plt.scatter(x, y)
    plt.title(name)
    plt.savefig(f"plots/graph/{name}_graph.png")
    print()


if __name__ == '__main__':
    swarm = generate_swarm()
    best_positions, best_adaptations = find_minimum(swarm)
    trucks = Encoding.decode(best_positions[-1])
    print(len(trucks), best_adaptations[-1])
    print(trucks)
    plt.plot(np.arange(ITERATIONS), best_adaptations)
    plt.figure()
    paths_x = [[DATA[customer][0] for customer in [0] + truck + [0]]
               for truck in trucks]
    paths_y = [[DATA[customer][1] for customer in [0] + truck + [0]]
               for truck in trucks]
    for x, y in zip(paths_x, paths_y):
        plt.plot(x, y, '--', linewidth=0.5)
        plt.scatter(x, y)
    plt.show()
