from ortools.sat.python import cp_model

from table import Table
from consts import Consts
from variables import Variables
from constraints import add_constraints
from solution_callback import SolutionCallback


class Optimizer:
    def __init__(self, consts: Consts, seed: int = 123) -> None:
        model = cp_model.CpModel()

        solver = cp_model.CpSolver()
        solver.parameters.random_seed = seed
        solver.parameters.enumerate_all_solutions = False
        solver.parameters.linearization_level = 0

        self._model = model
        self._solver = solver
        self._consts = consts

    def run(self) -> Table | None:
        variables = Variables(model=self._model, consts=self._consts)

        add_constraints(model=self._model, consts=self._consts, variables=variables)

        solution_callback = SolutionCallback(consts=self._consts, variables=variables)
        status = self._solver.solve(model=self._model, solution_callback=solution_callback)
        has_solution = status == cp_model.OPTIMAL or status == cp_model.FEASIBLE
        self._print_statistics()

        if not has_solution:
            return None
        return solution_callback.result_table

    def _print_statistics(self) -> None:
        print("\n-------- WallTime --------")
        print(f"{self._solver.wall_time:1f} s")
