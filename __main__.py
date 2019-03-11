from Polynomial import Polynomial
from Evolution import World
from Data import read_data

if __name__ == "__main__":
    w=World(0.05, 5, 10, read_data("pi.csv"))
    w.evol(100)