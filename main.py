from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables x and y
    x = solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')
    print('Number of variables =', solver.NumVariables())
if __name__ == '__main__':
   pywrapinit.CppBridge.InitLogging('basic_example.py')
   cpp_flags = pywrapinit.CppFlags()
   cpp_flags.logtostderr = True
   cpp_flags.log_prefix = False
   pywrapinit.CppBridge.SetFlags(cpp_flags)
   main()
