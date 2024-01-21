# November 2022
class Main:
    def __init__(self, num_particles, dimension, num_iterations, inertia_weight, cognitive_weight, social_weight):
        self.swarm = Swarm(num_particles, dimension)
        self.num_iterations = num_iterations
        self.inertia_weight = inertia_weight
        self.cognitive_weight = cognitive_weight
        self.social_weight = social_weight
    def optimize(self):
        for _ in range(self.num_iterations):
            for particle in self.swarm.particles:
                for i in range(len(particle.velocity)):
                    r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
                    cognitive_term = self.cognitive_weight * r1 * (particle.best_position[i] - particle.position[i])
                    social_term = self.social_weight * r2 * (self.swarm.global_best_position[i] - particle.position[i])
                    particle.velocity[i] = self.inertia_weight * particle.velocity[i] + cognitive_term + social_term
                particle.update_position()
                particle.fitness = self.evaluate_fitness(particle.position)
                if particle.fitness < particle.best_fitness:
                    particle.best_fitness = particle.fitness
                    particle.best_position = particle.position
            self.swarm.update_global_best()
    def evaluate_fitness(self, position):
        return sum(x**2 for x in position)
    def get_best_solution(self):
        return self.swarm.global_best_position
    def get_best_fitness(self):
        return self.swarm.global_best_fitness
