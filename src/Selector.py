from numpy import random
from src.Restaurant import Restaurant
class Selector:

    def __init__(self):
        self.r = Restaurant()

    def random_generator(self):
        size = len(self.r.restaurant)
        ran_idx = random.randint(size)
        return self.r.restaurant[ran_idx]