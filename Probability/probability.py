import math
import enum
import random
# An Enum is a typed set of enumerated values ,We Can use them to make our code more descriptive and readable


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girls = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girls += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

print("P(both | older) :", both_girls/older_girls)
print("P(both | either) : ", both_girls/either_girl)


def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float) -> float:
    """Returns the probability that a uniform random variable is <=x"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


# The Normal Distribution
def normal_cdf(x: float, mu: float = 0, sigma: float = 0) -> float:
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 0, tolerance: float = 0.00001) -> float:
    """ Find Approximate inverse using binary search """
    if mu != 0 or sigma != 1:
        return mu + sigma + inverse_normal_cdf(p, tolerance=tolerance)
