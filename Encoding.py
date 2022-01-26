import math
import numpy as np
from Params import DISTANCES, DATA, CAPACITY

X = 0
Y = 1
DEMAND = 2
READY_TIME = 3
DUE_DATE = 4
SERVICE_TIME = 5

indices = list(range(1, 101))


def can_travel(truck, capacity, time, customer):
    last = truck[-1] if len(truck) > 0 else 0
    customer_demand = DATA[customer][DEMAND]
    due_date = DATA[customer][DUE_DATE]
    travel_time = math.floor(DISTANCES[last][customer])

    return capacity >= customer_demand and time + travel_time <= due_date


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
        ready_time = DATA[nearest][READY_TIME]
        service_time = DATA[nearest][SERVICE_TIME]
        travel_time = math.floor(DISTANCES[current][nearest])
        current = nearest
        if time + travel_time < ready_time:
            time = ready_time
        else:
            time += travel_time
        time += service_time
        new_truck.append(nearest)
        copy.remove(nearest)
        if not can_travel(new_truck, np.inf, time, nearest):
            return truck.copy()

    return new_truck.copy() if total_distance(new_truck) < total_distance(truck) else truck.copy()


def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)


def total_distance(truck):
    copy = truck.copy()
    copy.insert(0, 0)
    copy.append(0)
    return sum([DISTANCES[copy[i]][copy[i + 1]] for i in range(len(copy) - 1)])


def extract_indices(customers):
    positions_with_indices = list(zip(customers, indices))
    positions_with_indices.sort(key=lambda x: x[0])
    return [x[1] for x in positions_with_indices]


def decode(position):
    customers = extract_indices(position)
    trucks = []

    for _ in range(100):  # bo 100 truckow
        truck = []
        time = 0
        capacity = CAPACITY
        prev_customer = 0
        for customer in customers:
            customer_demand = DATA[customer][DEMAND]
            ready_time = DATA[customer][READY_TIME]
            service_time = DATA[customer][SERVICE_TIME]
            travel_time = math.floor(DISTANCES[prev_customer][customer])
            if can_travel(truck, capacity, time, customer):
                if time + travel_time < ready_time:
                    time = ready_time
                else:
                    time += travel_time
                time += service_time
                capacity -= customer_demand
                prev_customer = customer
                truck.append(customer)
                customers.remove(customer)
        if len(truck) > 0:
            trucks.append(nearest_neighbour(truck))
            # trucks.append(truck)

    return trucks
