import numpy as np


def read_file(filename):
    prefix = filename[0:2] if len(filename) < 9 else filename[0:3]
    with open(f'files/{prefix}/{filename}') as f:
        return np.loadtxt(f, usecols=(1, 2, 3, 4, 5, 6))


if __name__ == '__main__':
    print(read_file('RC101.txt'))
