from typing import Callable
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


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A(as a Vector)"""
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """returns the j-th column of A(as a Vector)"""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols Matrix whose (i,j)-th entry in entry_fn(i,j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n indentity Matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]
