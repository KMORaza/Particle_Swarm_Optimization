# November 2022
class Swarm:
    def __init__(self, num_particles, dimension):
        self.particles = [Particle(dimension) for _ in range(num_particles)]
        self.global_best_position = self.get_global_best_position()
        self.global_best_fitness = float('inf')
    def get_global_best_position(self):
        best_particle = min(self.particles, key=lambda particle: particle.best_fitness)
        return best_particle.best_position
    def update_global_best(self):
        current_best_position = self.get_global_best_position()
        current_best_fitness = float('inf')
        for particle in self.particles:
            if particle.best_fitness < current_best_fitness:
                current_best_fitness = particle.best_fitness
                current_best_position = particle.best_position
        self.global_best_fitness = current_best_fitness
        self.global_best_position = current_best_position
    def __str__(self):
        return f"Global Best: {self.global_best_position}, Fitness: {self.global_best_fitness}"
