import numpy as np
import pandas as pd


class Table:
    def __init__(self, number_array: np.ndarray) -> None:
        assert number_array.shape == (9, 9)
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= 9

        self._number_array = number_array

    @property
    def number_df(self) -> pd.DataFrame:
        indexes = list(range(1, 10))
        columns = list(range(1, 10))

        return pd.DataFrame(
            data=self._number_array,
            index=indexes,
            columns=columns,
            dtype=int,
        )
