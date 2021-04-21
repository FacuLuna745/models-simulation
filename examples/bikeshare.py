#!/usr/bin/python

from modsim import *
from matplotlib import pyplot

np.random.seed()


def step(state, p1, p2):
    """Simulate one minute of time.

    state: bikeshare State object
    p1: probability of an um->comedor customer arrival
    p2: probability of a comedor->um customer arrival
    """
    if flip(p1):
        bike_to_comedor(state)

    if flip(p2):
        bike_to_um(state)


def bike_to_comedor(state):
    """Move one bike from um to comedor.

    state: bikeshare State object
    """
    if state.um > 0:
        state.um -= 1
        state.comedor += 1
    else:
        # no tenemos bicicletas
        state.um_vacio += 1


def bike_to_um(state):
    """Move one bike from comedor to um.

    state: bikeshare State object
    """
    if state.comedor > 0:
        state.comedor -= 1
        state.um += 1
    else:
        # no tenemos bicicletas
        state.comedor_vacio += 1


def decorate_bikeshare():
    """Add a title and label the axes."""
    decorate(title='um-comedor Bikeshare',
             xlabel='Time step (min)',
             ylabel='Number of bikes')


def run_simulation(state, p1, p2, num_steps):
    """Simulate the given number of time steps.
    
    state: State object
    p1: probability of an um->comedor customer arrival
    p2: probability of a comedor->um customer arrival
    num_steps: number of time steps
    """
    results = TimeSeries()
    for i in range(num_steps):
        step(state, p1, p2)
        results[i] = state.um

    plot(results, label='um')
    decorate_bikeshare()
    savefig('/tmp/grafico.jpg')


def main():
    bikeshare = State(um=10, comedor=2, um_vacio=0, comedor_vacio=0)

    #    run_simulation(bikeshare, 0.6, 0.2, 30)
    # metricas
    #    print(f"Um vacio: {bikeshare.um_vacio}")
    #    print(f"Comedor vacio: {bikeshare.comedor_vacio}")

    # barrido de parametros
    sweep_um = modsim.SweepSeries()
    sweep_comedor = modsim.SweepSeries()
    p1_array = linspace(0, 1, 11)
    print(p1_array)
    p2 = 0.5
    num_steps = 1000500
    for p1 in p1_array:
        run_simulation(bikeshare, p1, p2, num_steps)
        sweep_um[p1] = bikeshare.um_vacio
        sweep_comedor[p1] = bikeshare.comedor_vacio
        bikeshare.um_vacio = 0
        bikeshare.comedor_vacio = 0

    pyplot.clf()
    plot(sweep_um, label='um')
    plot(sweep_comedor, label='comedor')
    decorate_bikeshare()
    savefig('/tmp/sweep.jpg')


#        print(round(p1,2), bikeshare.um, bikeshare.um_vacio)


if __name__ == "__main__":
    main()

"""
Otra métrica:


"""
