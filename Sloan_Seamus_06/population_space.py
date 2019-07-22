import math
import random


class Population:
    x = None
    fitness = None

    def __init__(self, previous=0):
        self.x = random.randint(-10, 110)
        if previous != 0:
            self.x += self.x / previous
        self.fitness = self.evaluate()

    def evaluate(self):
        if self.x > 100:
            return -math.exp(-1) + (self.x - 100)*(self.x - 102)
        else:
            return -math.exp(-pow(self.x / 100, 2))

