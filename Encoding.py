import math
import reader

X = 0
Y = 1
DEMAND = 2
READY_TIME = 3
DUE_DATE = 4
SERVICE_TIME = 5

data = reader.read_file('R101.txt')

indices = list(range(1, 101))


def distance(x, y):
    return math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)


def total_distance(truck, data):
    truck.insert(0, 0)
    truck.append(0)
    return sum([distance((data[i][X], data[i][Y]), (data[i + 1][X], data[i + 1][Y])) for i in range(len(truck))])


def extract_indices(customers):
    positions_with_indices = list(zip(customers, indices))
    positions_with_indices.sort(key=lambda x: x[0])
    return [x[1] for x in positions_with_indices]


def decode(particle, data):
    # positions_with_indices = list(zip(particle.position, indices))
    # positions_with_indices.sort(key=lambda x: x[0])
    customers = extract_indices(particle.position)
    trucks = []
    prev_customer = (data[0][X], data[0][Y])
    truck = []
    capacity = particle.capacity
    time = 0

    while len(customers) > 0:
        customer = customers[0]
        customer_demand = data[customer][DEMAND]
        ready_time = data[customer][READY_TIME]
        due_date = data[customer][DUE_DATE]
        service_time = data[customer][SERVICE_TIME]
        customer_position = (data[customer][X], data[customer][Y])
        travel_time = math.floor(distance(prev_customer, customer_position))

        if capacity < customer_demand or time + travel_time > due_date:
            trucks.append(truck.copy())
            truck = []
            time = 0
            capacity = particle.capacity
            prev_customer = (data[0][X], data[0][Y])
            continue
        if time + travel_time < ready_time:
            time = ready_time
        else:
            time += travel_time
        time += service_time
        capacity -= customer_demand
        prev_customer = customer_position
        truck.append(customers.pop(0))
    trucks.append(truck)

    return trucks


def decode_from_position(position, particle_capacity):
    # positions_with_indices = list(zip(position, indices))
    # positions_with_indices.sort(key=lambda x: x[0])
    customers = extract_indices(position)
    trucks = []
    prev_customer = (data[0][X], data[0][Y])
    truck = []
    capacity = particle_capacity
    time = 0

    while len(customers) > 0:
        customer = customers[0]
        customer_demand = data[customer][DEMAND]
        ready_time = data[customer][READY_TIME]
        due_date = data[customer][DUE_DATE]
        service_time = data[customer][SERVICE_TIME]
        customer_position = (data[customer][X], data[customer][Y])
        travel_time = math.floor(distance(prev_customer, customer_position))

        if capacity < customer_demand or time + travel_time > due_date:
            trucks.append(truck.copy())
            truck = []
            time = 0
            capacity = particle_capacity
            prev_customer = (data[0][X], data[0][Y])
            continue
        if time + travel_time < ready_time:
            time = ready_time
        else:
            time += travel_time
        time += service_time
        capacity -= customer_demand
        prev_customer = customer_position
        truck.append(customers.pop(0))
    trucks.append(truck)

    return trucks
