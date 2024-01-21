# November 2022
import random
class Particle:
    def __init__(self, dimension):
        self.position = [random.uniform(-5, 5) for _ in range(dimension)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimension)]
        self.best_position = self.position
        self.fitness = float('inf')
        self.best_fitness = float('inf')
    def update_position(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
    def __str__(self):
        return f"Position: {self.position}, Fitness: {self.fitness}"
