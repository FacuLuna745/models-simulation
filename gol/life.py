import numpy as np
import time
import os


def read_matrix():
    return np.loadtxt('seed.txt', delimiter=' ', dtype='int')


def check_neighbor(matrix, x, y):
    neighbor = matrix[x % len(matrix)][(y - 1) % len(matrix)] + \
               matrix[x % len(matrix)][(y + 1) % len(matrix)] + \
               matrix[(x - 1) % len(matrix)][(y - 1) % len(matrix)] + \
               matrix[(x - 1) % len(matrix)][y % len(matrix)] + \
               matrix[(x - 1) % len(matrix)][(y + 1) % len(matrix)] + \
               matrix[(x + 1) % len(matrix)][(y - 1) % len(matrix)] + \
               matrix[(x + 1) % len(matrix)][y % len(matrix)] + \
               matrix[(x + 1) % len(matrix)][(y + 1) % len(matrix)]
    return neighbor


def survival(matrix):
    matrix_aux = np.copy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            counter = check_neighbor(matrix, x, y)
            if matrix[x][y] == 1 and (counter < 2 or counter > 3):
                matrix_aux[x][y] = 0
            elif matrix[x][y] == 0 and counter == 3:
                matrix_aux[x][y] = 1
    return np.copy(matrix_aux)


def check_life_dead(matrix):
    life = 0
    dead = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 0:
                dead += 1
            elif matrix[x][y] == 1:
                life += 1
    return life, dead


def check_gen(counter_gen):
    return counter_gen + 1


def check_running_gen(matrix):
    counter_zero = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 0:
                counter_zero += 1
    if counter_zero == (len(matrix) * len(matrix)):
        print("Se salio de la ejecución ya que no hay mas generaciones")
        return False
    else:
        return True


if __name__ == '__main__':
    run = True
    matrix = read_matrix()
    gen = 0
    try:
        while run:
            check = check_life_dead(matrix)
            gen = check_gen(gen)
            print(f"{matrix} \nCeldas vivas: {check[0]} \nCeldas muertas: {check[1]} \nGeneración: {gen}")
            matrix = survival(matrix)
            time.sleep(1)
            os.system('clear')
            run = check_running_gen(matrix)
    except (KeyboardInterrupt):
        print("\n La ejecución se cancelo")
