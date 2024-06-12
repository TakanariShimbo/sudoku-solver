import numpy as np
import pandas as pd


class Table:
    def __init__(self, number_array: np.ndarray) -> None:
        max_number = max(self.numbers)

        assert number_array.shape == self.size
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= max_number

        self._number_array = number_array

    @property
    def h_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def v_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def size(self) -> tuple[int, int]:
        return len(self.h_positions), len(self.v_positions)

    @property
    def numbers(self) -> list[int]:
        return list(range(1, 10))

    @property
    def h_grid_positions(self) -> list[int]:
        return list(range(1, 4))

    @property
    def v_grid_positions(self) -> list[int]:
        return list(range(1, 4))

    @property
    def h_positions_in_grid(self) -> list[int]:
        return list(range(1, 4))

    @property
    def v_positions_in_grid(self) -> list[int]:
        return list(range(1, 4))

    @property
    def number_df(self) -> pd.DataFrame:
        return pd.DataFrame(
            data=self._number_array,
            index=self.v_positions,
            columns=self.h_positions,
            dtype=int,
        )

    def get_fixed_number(self, h_position: int, v_position: int) -> int | None:
        val = self.number_df.loc[v_position, h_position]
        if val == 0:
            return None
        else:
            return int(val)
