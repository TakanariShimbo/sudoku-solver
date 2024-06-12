import numpy as np

from table import Table
from consts import Consts
from optimizer import Optimizer


fixed_number_array = np.array(
    [
        [0, 8, 0, 4, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 1, 3, 0],
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 5, 0, 0],
        [7, 0, 5, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [5, 2, 0, 3, 0, 0, 0, 7, 6],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ],
    dtype=int,
)
fixed_table = Table(number_array=fixed_number_array)
consts = Consts(fixed_table=fixed_table)
optimizer = Optimizer(consts=consts, seed=123)
result_table = optimizer.run()


print("\n-------- Probrem --------")
print(fixed_table.number_df)

print("\n-------- Solution --------")
if result_table:
    print(result_table.number_df)
else:
    print("Not found")

print()
