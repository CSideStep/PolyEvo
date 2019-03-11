from typing import List
from Polynomial import Polynomial, create_random_polynomial
from math import sqrt
from random import choices, random, randint
class World:
    data:List[List[float]]
    population_size:int
    population:List[Polynomial]
    mutation_rate:float
    poly_length:int
    min_value:float
    max_value:float

    def __init__(self, mutation_rate:float, poly_length:int, pop_size:int, data:List[List[float]],min_value:float=-1000.0, max_value:float=1000.0):
        self.data=data
        self.population_size=pop_size
        self.poly_length=poly_length
        self.mutation_rate=mutation_rate
        self.min_value=min_value
        self.max_value=max_value
        self.population=[create_random_polynomial(poly_length, min_value, max_value) for _ in range(self.population_size)]
        self.best_poly=[self.population[0], self.eval_poly(self.population[0])]
    def eval_poly(self, poly:Polynomial):
        error=sqrt(sum([(float(dp[1])-poly.calculate(float(dp[0])))**2 for dp in self.data]))
        return error

    def create_child(self, p1:Polynomial, p2:Polynomial, s1:float, s2:float):
        denom=s1+s2
        cs=[]
        for i in range(self.poly_length):
            if random() <= self.mutation_rate:
                cs.append(self.min_value + random()*(self.max_value-self.min_value))
            else:
                cs.append(choices([p1.coefficients[i], p2.coefficients[i]], weights=[s1/denom, s2/denom])[0])
        return Polynomial(cs)

    def next_gen(self):
        eval_pairs=[]
        errors=[]
        for poly in self.population:
            error=self.eval_poly(poly)  
            eval_pairs.append([poly, error])
            errors.append(error)
        eval_pairs.sort(key=lambda x: x[1])
        new_pop=[eval_pairs[i][0] for i in range(int(self.population_size/2))]
        children=[]
        for _ in range(int(self.population_size/2)):
            ip1=randint(0, int(self.population_size/2)-1)
            ip2=randint(0, int(self.population_size/2)-1)
            children.append(self.create_child(eval_pairs[ip1][0], eval_pairs[ip2][0], eval_pairs[ip1][1], eval_pairs[ip2][1]))
        self.population=children+new_pop   
        self.best_poly=eval_pairs[0]
        print(f"{sum(errors)/self.population_size} avg error")
    def evol(self, n):
        for i in range(100):
            self.next_gen()
            print(f"{self.best_poly[1]}, ({100*i/n}%)")
        return self.best_poly[0].coefficients
                      