from typing import List
from random import random

def create_random_polynomial(length:int, min_value:float, max_value:float):
    return Polynomial([min_value + random()*(max_value-min_value) for i in range(length)])

class Polynomial:
    coefficients:List[float]

    def __init__(self, cs:List[float]):
        self.coefficients=cs

    def calculate(self, x):
        rtn=0
        for i, c in enumerate(self.coefficients):
            rtn += c*(x**i)
        return rtn


