import numpy as np
from scipy.spatial import distance


def read_file(filename):
    prefix = filename[0:2] if len(filename) < 9 else filename[0:3]
    with open(f'files/{prefix}/{filename}') as f:
        return np.loadtxt(f, usecols=(1, 2, 3, 4, 5, 6))


def distance_array(filename):
    data = None
    prefix = filename[0:2] if len(filename) < 9 else filename[0:3]
    with open(f'files/{prefix}/{filename}') as f:
        data = np.loadtxt(f, usecols=(1, 2))
    data = [tuple((x[0], x[1])) for x in data]
    return distance.squareform(distance.pdist(data, metric='euclidean'))


if __name__ == '__main__':
    print(distance_array('RC101.txt').tolist())
