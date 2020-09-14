from typing import Callable
from LinearAlgebra import Vector, dot


def sum_of_squares(v: Vector) -> float:
    """Computes the sum of squared elements in v"""
    return dot(v, v)


def difference_quotient(f: Callable[[float], [float]], x: float, h: float) -> float:
    return (f(x+h) - f(x))/h


def square(x: float) -> float:
    return x*x


def derivative(x: float) -> float:
    return 2*x
