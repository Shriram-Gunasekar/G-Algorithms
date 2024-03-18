import random

# Define the items (value, weight) and knapsack capacity
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
knapsack_capacity = 50

# Initialize parameters
population_size = 50
num_generations = 100
mutation_rate = 0.1
tournament_size = 3
elite_size = 2

# Generate initial population
def generate_individual():
    return [random.randint(0, 1) for _ in range(len(items))]

population = [generate_individual() for _ in range(population_size)]

# Fitness function
def fitness_function(individual):
    total_value = sum(item[0] * bit for item, bit in zip(items, individual))
    total_weight = sum(item[1] * bit for item, bit in zip(items, individual))
    if total_weight > knapsack_capacity:
        return 0  # Penalize solutions that exceed weight limit
    else:
        return total_value

# Genetic Algorithm loop
for generation in range(num_generations):
    # Evaluate fitness
    fitness_scores = [fitness_function(individual) for individual in population]
    sorted_indices = sorted(range(len(fitness_scores)), key=lambda k: fitness_scores[k], reverse=True)
    sorted_population = [population[i] for i in sorted_indices]

    # Select parents using tournament selection
    parents = []
    for _ in range(population_size):
        tournament = random.sample(sorted_population, tournament_size)
        winner = max(tournament, key=fitness_function)
        parents.append(winner)

    # Perform crossover (single-point crossover)
    offspring = []
    for i in range(0, population_size, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        crossover_point = random.randint(1, len(items) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.extend([child1, child2])

    # Mutate offspring
    for i in range(population_size):
        if random.random() < mutation_rate:
            mutate_index = random.randint(0, len(items) - 1)
            offspring[i][mutate_index] ^= 1  # Flip the bit (0 to 1 or 1 to 0)

    # Elitism: Select the best individuals to survive
    population = sorted_population[:elite_size] + offspring[:population_size - elite_size]

# Get the best individual (solution)
best_individual = max(population, key=fitness_function)
best_fitness = fitness_function(best_individual)

print("Best individual (solution):", best_individual)
print("Best fitness (total value):", best_fitness)
