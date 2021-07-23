import itertools
import random
from pandas import read_table
import numpy

table = read_table("datosPracticaMontecarlo.txt", delim_whitespace=True, header=None, index_col=0)
table.columns = ['infoHistory']
diasProximos = 100

# Ordeno la columna de menor a mayor
table.sort_values(by=['infoHistory'], ascending=True, inplace=True)

# Calculo del total
total = float(table.sum())

# Calculo de media
mean = float(table.mean())
print(f"La media original es: {mean}")

# Calculo de varianza
var = float(table.var())
print(f"La varianza original es: {var}")

# Calculo del desvio estandar
desvStd = float(table.std())
print(f"El desvio estandar original es: {desvStd}")

# Calculo de minimos y maximos
min = float(table.min())
max = float(table.max())
print(f"El minimo original es: {min} y el maximo original es: {max}")

# Calculo de la distribución acumulada
distrAcumulada = list(itertools.accumulate(table['infoHistory']))

# Calculo de la distribución acumulada normalizada
distrNormalizado = []
for i in distrAcumulada:
    distrNormalizado.append(i / total)

print("\n\033[;36m" + "-------------------Aplicación del metodo Montecarlo-------------------")
# Montecarlo para los valores random
listRandom = []
valuesEstimated = []
for i in range(diasProximos):
    listRandom.append(random.uniform(0, 1))

for r in listRandom:
    for index, value in enumerate(distrNormalizado):
        if value > r:
            valuesEstimated.append(table.at[index, "infoHistory"])
            break
print(f"Los datos random generados son: {valuesEstimated}")

historyEstimated = numpy.array(valuesEstimated)

# Comprobación del método Montecarlo
# Calculo de la media con respecto a los datos obtenidos
meanEstimated = numpy.mean(historyEstimated)
print(f"\nLa media con respecto a los datos obtenidos es: {meanEstimated}")

# Calculo de la varianza con respecto a los datos obtenidos
varEstimated = numpy.var(historyEstimated)
print(f"La varianza con respecto a los datos obtenidos es: {varEstimated}")

# Calculo del desvió estándar con respecto a los datos obtenidos
stdEstimated = numpy.std(historyEstimated)
print(f"La media estandar con respecto a los datos obtenidos es: {stdEstimated}")
