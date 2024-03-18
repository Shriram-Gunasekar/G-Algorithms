import random

# Parameters
population_size = 50
chromosome_length = 10
mutation_rate = 0.1
num_generations = 100

# Initialize population
def initialize_population():
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

# Fitness evaluation
def evaluate_fitness(chromosome):
    return sum(chromosome)

# Tournament selection
def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    return max(selected, key=evaluate_fitness)

# Single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutate(chromosome):
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Genetic algorithm
def genetic_algorithm():
    population = initialize_population()
    for generation in range(num_generations):
        # Evaluate fitness
        fitness_scores = [evaluate_fitness(chromosome) for chromosome in population]
        best_individual = max(population, key=evaluate_fitness)
        print(f"Generation {generation + 1}: Best Fitness = {evaluate_fitness(best_individual)}, Best Individual = {best_individual}")

        # Selection and crossover
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        # Elitism: Keep the best individual from the previous generation
        new_population.append(best_individual)

        # Update population
        population = new_population

# Run the genetic algorithm
genetic_algorithm()
