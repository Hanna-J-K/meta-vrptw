import reader

FILENAME = 'RC201.txt'
CAPACITY = 1000
DATA = reader.read_file(FILENAME)
DISTANCES = reader.distance_array(FILENAME).tolist()


def refresh_data(name, capacity):
    global FILENAME
    global CAPACITY
    global DATA
    global DISTANCES
    FILENAME = name
    CAPACITY = capacity
    DATA = reader.read_file(FILENAME)
    DISTANCES = reader.distance_array(FILENAME).tolist()
