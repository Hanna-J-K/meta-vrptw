from Swarm import draw_swarm

if __name__ == "__main__":
    names = ['C101.txt', 'C102.txt', 'C103.txt',     # 200
             'C201.txt', 'C202.txt', 'C203.txt',     # 700
             'R101.txt', 'R102.txt', 'R103.txt',     # 200
             'R201.txt', 'R202.txt', 'R203.txt',     # 1000
             'RC101.txt', 'RC102.txt', 'RC103.txt',  # 200
             'RC201.txt', 'RC202.txt', 'RC205.txt']  # 1000
    capacities = [200, 200, 200,
                  700, 700, 700,
                  200, 200, 200,
                  1000, 1000, 1000,
                  200, 200, 200,
                  1000, 1000, 1000]

    for name, capacity in zip(names, capacities):
        draw_swarm(name, capacity)
