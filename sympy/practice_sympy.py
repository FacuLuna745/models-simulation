import sympy as s

if __name__ == '__main__':
    # Se asignan los símbolos y la función
    alpha, beta, t = s.symbols("alpha beta t")
    C1, t0 = s.symbols("C1 t0")
    f = s.Function('f')

    # Se deriva la función con respecto a t
    dfdt = s.diff(f(t), t)

    # Se define la ecuación a resolver
    eq = s.Eq(dfdt, alpha * f(t) + beta * f(t) ** 2)
    solution = s.dsolve(eq)

    # Se obtiene el lado derecho, que nos permite determinar el valor del C1
    # al aplicar las condiciones de contorno
    sol_g = solution.rhs

    # Se aplican las condiciones de contorno
    sol_t0 = sol_g.subs(t, 0)

    # Se obtiene C1
    condition_ini = s.Eq(sol_t0, t0)
    solutions = s.solve(condition_ini, C1)
    value_C1 = solutions[0]

    # Solución particular
    sol_part = solution.subs(C1, value_C1)

    # La simplificación es:
    solution_part_simplify = s.simplify(sol_part)
    print(f"La solución particular simplificada es: {solution_part_simplify}")

    # Se puede verificar con la siguiente linea:
    print(f"Cuando t=0: {solution_part_simplify.subs(t, 0)}")

