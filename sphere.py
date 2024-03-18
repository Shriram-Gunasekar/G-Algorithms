import random
import numpy as np

# Define the objective function (Sphere function)
def sphere_function(x):
    return sum(xi**2 for xi in x)

# Initialize parameters
num_dimensions = 5  # Number of dimensions
population_size = 50
num_generations = 100
mutation_rate = 0.1
tournament_size = 3
elite_size = 2

# Generate initial population
population = [np.random.uniform(-5.12, 5.12, num_dimensions) for _ in range(population_size)]

# Genetic Algorithm loop
for generation in range(num_generations):
    # Evaluate fitness
    fitness_scores = [sphere_function(individual) for individual in population]
    sorted_indices = np.argsort(fitness_scores)
    sorted_population = [population[i] for i in sorted_indices]

    # Select parents using tournament selection
    parents = []
    for _ in range(population_size):
        tournament = random.sample(sorted_population, tournament_size)
        winner = min(tournament, key=lambda x: sphere_function(x))
        parents.append(winner)

    # Perform crossover (two-point crossover)
    offspring = []
    for i in range(0, population_size, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        crossover_point1 = random.randint(1, num_dimensions - 2)
        crossover_point2 = random.randint(crossover_point1 + 1, num_dimensions - 1)
        child1 = np.concatenate((parent1[:crossover_point1], parent2[crossover_point1:crossover_point2], parent1[crossover_point2:]))
        child2 = np.concatenate((parent2[:crossover_point1], parent1[crossover_point1:crossover_point2], parent2[crossover_point2:]))
        offspring.extend([child1, child2])

    # Mutate offspring
    for i in range(population_size):
        if random.random() < mutation_rate:
            mutate_index = random.randint(0, num_dimensions - 1)
            offspring[i][mutate_index] += np.random.uniform(-0.5, 0.5)  # Mutation by adding a random value

    # Elitism: Select the best individuals to survive
    population = sorted_population[:elite_size] + offspring[:population_size - elite_size]

# Get the best individual
best_individual = min(population, key=lambda x: sphere_function(x))
best_fitness = sphere_function(best_individual)

print("Best individual:", best_individual)
print("Best fitness:", best_fitness)
