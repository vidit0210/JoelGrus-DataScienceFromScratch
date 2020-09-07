from typing import Tuple
Matrix = List[List[float]]

# A has 2 rowa and 3 coloumns
A = [[1, 2, 3], [4, 5, 6]]

# B has 3 rows and 2 coloumns
B = [[1, 2], [3, 4], [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns number of rows and cols of A"""
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
