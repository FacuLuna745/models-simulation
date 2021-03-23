import numpy as np

seed = np.loadtxt('seed.txt', delimiter=' ', dtype="int")


# def search_one():
#    for i in range(len(seed)):
#        for j in range(len(seed[i])):
#            if seed[i][j] == 1:
#                return i, j

def search(seed):
    positions = np.array(np.where(seed == 1)).tolist()
    positions_one = []
    for i in range(len(positions[0])):
        positions_one.append([positions[0][i], positions[1][i]])
    return positions_one


def survival(seed, position):
    neighbor = [[position[0], position[1] - 1], [position[0], position[1] + 1],
                [position[0] - 1, position[1] - 1], [position[0] - 1, position[1]], [position[0] - 1, position[1] + 1],
                [position[0] + 1, position[1] - 1], [position[0] + 1, position[1]], [position[0] + 1, position[1] + 1]]

    for i in range(len(neighbor)):
        values = neighbor[i]
        if seed[values[0]][values[1]] == 1:



survival(seed, [3, 5])
# for i in range(len(search(seed))):
#    print(f"La posicion del {i + 1}° uno es:{search(seed)[i]}")
