import reader

FILENAME = 'RC201.txt'
CAPACITY = 1000
DATA = reader.read_file(FILENAME)
DISTANCES = reader.distance_array(FILENAME).tolist()
