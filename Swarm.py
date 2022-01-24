import numpy as np
from Fitness import fitness
from Particle import Particle
import matplotlib.pyplot as plt
import random
from Crossbreed import crossover

POPULATION = 50
ITERATIONS = 100


def generate_swarm(capacity):
    return [Particle(capacity) for _ in range(POPULATION)]


def find_minimum(swarm):
    crossover_probability = 0.9
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
        best_adaptations.append(global_best_adaptation)
        best_positions.append(global_best_position)

    return best_positions, best_adaptations


if __name__ == '__main__':
    swarm = generate_swarm(200)
    best_positions, best_adaptations = find_minimum(swarm)
    # for adaptation, position in zip(best_adaptations, best_positions):
    #     print(f"{adaptation} total, {len([1])} trucks")
    print(len(best_positions[-1]), best_adaptations[-1])
    plt.plot(np.arange(ITERATIONS), best_adaptations)
    plt.show()
