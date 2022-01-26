import math
import reader
import numpy as np
from Distance import DISTANCES

X = 0
Y = 1
DEMAND = 2
READY_TIME = 3
DUE_DATE = 4
SERVICE_TIME = 5

data = reader.read_file('R101.txt')

indices = list(range(1, 101))


def can_travel(truck, capacity, time, customer):
    last = truck[-1] if len(truck) > 0 else 0
    last_customer_position = (data[last][X], data[last][Y])
    customer_demand = data[customer][DEMAND]
    due_date = data[customer][DUE_DATE]
    customer_position = (data[customer][X], data[customer][Y])
    travel_time = math.floor(
        distance(last_customer_position, customer_position))

    return capacity >= customer_demand or time + travel_time <= due_date


def nearest_neighbour(truck):
    copy = truck.copy()
    new_truck = []
    time = 0
    current = 0
    nearest = 0
    for _ in range(len(truck)):
        nearest = copy[0]
        for customer in copy:
            if can_travel(new_truck, np.inf, time, customer) and DISTANCES[current][customer] < DISTANCES[current][nearest]:
                nearest = customer
        ready_time = data[nearest][READY_TIME]
        service_time = data[nearest][SERVICE_TIME]
        travel_time = DISTANCES[current][nearest]
        current = nearest
        if time + travel_time < ready_time:
            time = ready_time
        else:
            time += travel_time
        time += service_time
        new_truck.append(nearest)
        copy.remove(nearest)
        if not can_travel(new_truck, np.inf, time, nearest):
            return truck

    return new_truck if total_distance(new_truck, data) < total_distance(truck, data) else truck


def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)


def total_distance(truck, data):
    truck.insert(0, 0)
    truck.append(0)
    return sum([distance((data[truck[i]][X], data[truck[i]][Y]), (data[truck[i + 1]][X], data[truck[i + 1]][Y])) for i in range(len(truck) - 1)])


def extract_indices(customers):
    positions_with_indices = list(zip(customers, indices))
    positions_with_indices.sort(key=lambda x: x[0])
    return [x[1] for x in positions_with_indices]


def decode(particle, data):
    customers = extract_indices(particle.position)
    trucks = []
    prev_customer = (data[0][X], data[0][Y])
    truck = []
    capacity = particle.capacity
    time = 0

    for _ in range(100):  # bo 100 truckow
        truck = []
        time = 0
        capacity = particle.capacity
        prev_customer = (data[0][X], data[0][Y])
        for customer in customers:
            customer_demand = data[customer][DEMAND]
            ready_time = data[customer][READY_TIME]
            service_time = data[customer][SERVICE_TIME]
            customer_position = (data[customer][X], data[customer][Y])
            travel_time = math.floor(
                distance(prev_customer, customer_position))
            if can_travel(truck, capacity, time, customer):
                if time + travel_time < ready_time:
                    time = ready_time
                else:
                    time += travel_time
                time += service_time
                capacity -= customer_demand
                prev_customer = customer_position
                truck.append(customer)
                customers.remove(customer)
        if len(truck) > 0:
            trucks.append(nearest_neighbour(truck))
            # trucks.append(truck)

    return trucks


def decode_from_position(position, particle_capacity):
    customers = extract_indices(position)
    trucks = []
    prev_customer = (data[0][X], data[0][Y])
    truck = []
    capacity = particle_capacity
    time = 0

    for _ in range(100):  # bo 100 truckow
        truck = []
        time = 0
        capacity = particle_capacity
        prev_customer = (data[0][X], data[0][Y])
        for customer in customers:
            customer_demand = data[customer][DEMAND]
            ready_time = data[customer][READY_TIME]
            due_date = data[customer][DUE_DATE]
            service_time = data[customer][SERVICE_TIME]
            customer_position = (data[customer][X], data[customer][Y])
            travel_time = math.floor(
                distance(prev_customer, customer_position))
            if capacity < customer_demand or time + travel_time > due_date:
                continue
            if time + travel_time < ready_time:
                time = ready_time
            else:
                time += travel_time
            time += service_time
            capacity -= customer_demand
            prev_customer = customer_position
            truck.append(customer)
            customers.remove(customer)
        if len(truck) > 0:
            trucks.append(nearest_neighbour(truck)[1:-1])

    return trucks
