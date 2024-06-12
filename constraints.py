from ortools.sat.python import cp_model

from consts import Consts
from variables import Variables


def add_constraints(model: cp_model.CpModel, consts: Consts, variables: Variables) -> None:
    # -----------------------------------------
    # One number per cell (h, v) constraint
    # -----------------------------------------
    for h_position in consts.h_positions:
        for v_position in consts.v_positions:

            is_assigned_vars: list[cp_model.BoolVarT] = []
            for number in consts.numbers:
                is_assigned_var = variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)
                is_assigned_vars.append(is_assigned_var)

            model.add_exactly_one(is_assigned_vars)

    # -----------------------------------------
    # Vartical constraint
    # -----------------------------------------
    for number in consts.numbers:
        for h_position in consts.h_positions:

            is_assigned_vars: list[cp_model.BoolVarT] = []
            for v_position in consts.v_positions:
                is_assigned_var = variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)
                is_assigned_vars.append(is_assigned_var)

            model.add_exactly_one(is_assigned_vars)

    # -----------------------------------------
    # Horizontal constraint
    # -----------------------------------------
    for number in consts.numbers:
        for v_position in consts.v_positions:

            is_assigned_vars: list[cp_model.BoolVarT] = []
            for h_position in consts.h_positions:
                is_assigned_var = variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)
                is_assigned_vars.append(is_assigned_var)

            model.add_exactly_one(is_assigned_vars)

    # -----------------------------------------
    # 3x3 subgrid constraint
    # -----------------------------------------
    for number in consts.numbers:
        for h_grid_position in consts.h_grid_positions:
            for v_grid_position in consts.v_grid_positions:

                is_assigned_vars: list[cp_model.BoolVarT] = []
                for h_position_in_grid in consts.h_positions_in_grid:
                    for v_position_in_grid in consts.v_positions_in_grid:
                        is_assigned_var = variables.get_is_assigned_var_(
                            h_grid_position=h_grid_position,
                            v_grid_position=v_grid_position,
                            h_position_in_grid=h_position_in_grid,
                            v_position_in_grid=v_position_in_grid,
                            number=number,
                        )
                        is_assigned_vars.append(is_assigned_var)

                model.add_exactly_one(is_assigned_vars)

    # -----------------------------------------
    # Fixed constraint
    # -----------------------------------------
    for v_position in consts.v_positions:
        for h_position in consts.h_positions:

            fixed_number = consts.get_fixed_number(h_position=h_position, v_position=v_position)
            if fixed_number == None:
                continue

            is_assigned_var = variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=fixed_number)
            model.add(is_assigned_var == 1)