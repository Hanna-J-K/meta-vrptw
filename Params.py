import reader

FILENAME = 'R101.txt'
CAPACITY = 200
DATA = reader.read_file(FILENAME)
DISTANCES = reader.distance_array(FILENAME).tolist()
