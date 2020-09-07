from typing import Callable
from typing import Tuple, List
import math
from typing import List

Vector = List[float]
height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding element"""
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum of all corresponding elements"""
    assert vectors, "No Vectors provided"
    # Check all the vectors provided are of same size
    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors), "Different sizes in the vector"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * vi for vi in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """computes Element wise Average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> Vector:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    """Return v_1 * v1 + ..... + v_n * _vn"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14


def magnitude(v: Vector) -> float:
    """Returns the magnitude of v"""
    return math.sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


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
