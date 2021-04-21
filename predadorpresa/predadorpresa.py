import matplotlib.pyplot as plt
import os


def change_parameter():
    os.system("clear")
    print("\x1b[1;33m" + "Cambio de parametros: ")
    delta_t = float(input("Ingrese el incremento de tiempo en semanas: "))
    hares = int(input("Ingrese la cantidad de liebres: "))
    fox = int(input("Ingrese la cantidad de zorros: "))
    hares_rate = float(input("Ingrese la tasa de crecimiento de las liebres: "))
    fox_rate = float(input("Ingrese la tasa de supervivencia de los zorros: "))
    terrain_capacity = int(input("Ingrese la capacidad del terreno: "))
    week = int(input("Ingrese la cantidad de semanas: "))

    return delta_t, hares, fox, hares_rate, fox_rate, terrain_capacity, week


def parameter():
    delta_t = 1
    hares = 2500
    fox = 2
    hares_rate = 0.08
    fox_rate = 0.2
    terrain_capacity = 1400
    week = 500

    return delta_t, hares, fox, hares_rate, fox_rate, terrain_capacity, week


def graphic(total_hares, total_fox):
    # Diagrama de fase
    plt.plot(total_hares, total_fox)
    plt.title("Diagrama de fase")
    plt.xlabel("Población de liebres")
    plt.ylabel("Población de zorros")
    plt.savefig('graphic/phase.jpg')
    plt.grid(True)
    plt.show()

    # Diagrama de población
    plt.title("Diagrama de la variación en la población")
    plt.xlabel("Semanas")
    plt.ylabel("Población de liebres")
    plt.plot(total_hares, label="Liebres", color="blue")
    plt.legend(loc='upper right', bbox_to_anchor=(0.3, 0.1, 0.5, 0.5))
    plt.twinx()
    plt.ylabel("Población de zorros")
    plt.plot(total_fox, label="Zorros", color="brown")
    plt.legend(loc='upper right', bbox_to_anchor=(0.3, 0.2, 0.5, 0.5))
    plt.grid(True)
    plt.savefig('graphic/population.jpg')
    plt.show()


def system(parameter):
    total_hares = []
    total_fox = []
    for i in range(parameter[6]):
        terrain_current = parameter[5] - parameter[1]
        increment_hares = (terrain_current / parameter[5]) * parameter[3] * parameter[1]
        decrease_fox = parameter[4] * parameter[2]
        hunting = parameter[2] * parameter[1]
        parameter[1] = parameter[1] + parameter[0] * (increment_hares - 0.002 * hunting)
        parameter[2] = parameter[2] + parameter[0] * (0.0004 * hunting - decrease_fox)
        total_hares.append(parameter[1])
        total_fox.append(parameter[2])

    graphic(total_hares, total_fox)


if __name__ == '__main__':
    print("\x1b[1;33m" + "BIENVENIDO A PRESA-PREDADOR")
    menu_option = input(
        "\x1b[1;33m" + "Desea cargar los parametros? Si no se ejecutara con los parametros por defecto... y / n: \n")
    if menu_option == 'y' or menu_option == 'Y':
        params = list(change_parameter())
        system(params)
    else:
        params = list(parameter())
        system(params)
    print("\033[;36m" + "Ademas de mostrar el grafico, los mismos fueron guardados en la carpeta predadorpresa/graphic")
