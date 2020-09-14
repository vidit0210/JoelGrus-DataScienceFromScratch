from LinearAlgebra import vector_mean
from LinearAlgebra import distance, add, scalar_multiply
import random
import matplotlib.pyplot as plt
from typing import Callable
from LinearAlgebra import Vector, dot


def sum_of_squares(v: Vector) -> float:
    """Computes the sum of squared elements in v"""
    return dot(v, v)


def difference_quotient(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x+h) - f(x))/h


def square(x: float) -> float:
    return x*x


def derivative(x: float) -> float:
    return 2*x


xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

plt.title("Actual Derivatives vs estimates")
plt.plot(xs, actuals, 'rx', label='Actual')
plt.plot(xs, estimates, 'b+', label="Estimate")
plt.legend(loc=9)
plt.show()


def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float) -> float:
    """Returns the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w)-f(v))/h


def estimate_gradient(f: Callable[[Vector], float], v: Vector, h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves step size in the gradient direction from v"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]


# Pick a random starting point
v = [random.uniform(-10, 10) for i in range(3)]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)
    print(epoch, v)

# V should be close to 0
assert distance(v, [0, 0, 0]) < 0.001, "Distance Assertion"

# using Gradient Descent to fit the models
inputs = [(x, 20*x+5) for x in range(-50, 50)]


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = (predicted - y)
    squared_error = error ** 2
    grad = [2 * error * x, 2*error]
    return grad

# Approaching Mean Squared Error


theta = [random_uniform(-1, 1), random.uniform(-1, 1)]
learning_rate = 0.001

for epoch in range(5000):
    # compute the ector mran of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
    # Take a step in that direction..
    theta = gradient_step(theta, grad, -learning_rate)
    print(epoch, theta)
