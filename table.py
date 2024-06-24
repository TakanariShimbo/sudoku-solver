import numpy as np
import pandas as pd


class Table:
    def __init__(self, number_array: np.ndarray) -> None:
        assert number_array.shape == self.table_size
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= max(self.numbers)

        self._number_array = number_array

    @classmethod
    def from_number_df(cls, number_df: pd.DataFrame) -> "Table":
        return cls(number_array=number_df.values)

    @classmethod
    def from_number_dict(cls, number_dict: dict[int, dict[int, int]]) -> "Table":
        number_df = pd.DataFrame(data=number_dict)
        return cls.from_number_df(number_df=number_df)

    @property
    def numbers(self) -> list[int]:
        return list(range(1, 10))

    @property
    def h_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def v_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def table_size(self) -> tuple[int, int]:
        return len(self.v_positions), len(self.h_positions)

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
    def grid_size(self) -> tuple[int, int]:
        return len(self.v_positions_in_grid), len(self.h_positions_in_grid)

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
