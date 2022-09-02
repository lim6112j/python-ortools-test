from ortools.linear_solver import pywraplp
def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    infinity = solver.infinity()
    x = solver.IntVar(0.0, infinity, 'x')
    y = solver.IntVar(0.0, infinity, 'y')
    print('Number of variables = ', solver.NumVariables())
    solver.Add(x + 7 * y <= 17.5)
    solver.Add(x <= 3.5)
    print('Number of constraints =', solver.NumConstraints())
    solver.Maximize(x + 10 * y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value = ', solver.Objective().Value())
        print('x = ', x.solution_value())
        print('y = ', y.solution_value())
    else:
        print('The problem does not have an optimal solution')

    print('\nAdvaned usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

if __name__ == '__main__':
    main()
