import numpy as np

seed = np.loadtxt('seed.txt', delimiter=' ', dtype="int")
counter = 0


def search(seed):
    positions = np.array(np.where(seed == 1)).tolist()
    positions_one = []
    for i in range(len(positions[0])):
        positions_one.append([positions[0][i], positions[1][i]])
    return positions_one


def survival(seed, position, counter_one):
    neighbor = [[position[0], position[1] - 1], [position[0], position[1] + 1],
                [position[0] - 1, position[1] - 1], [position[0] - 1, position[1]], [position[0] - 1, position[1] + 1],
                [position[0] + 1, position[1] - 1], [position[0] + 1, position[1]], [position[0] + 1, position[1] + 1]]

    for i in range(len(neighbor)):
        values = neighbor[i]
        if seed[values[0]][values[1]] == 1:
            counter_one += 1

    if counter_one > 3 or counter_one < 2:
        seed[position[0]][position[1]] = 0

    return seed


# pos = search(seed)
# for i in range(len(pos)):
#    seed = survival(seed, pos[i], counter)

# print(seed)

