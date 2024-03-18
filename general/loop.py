def genetic_algorithm(population_size, chromosome_length, generations, mutation_rate, tournament_size):
    population = create_population(population_size, chromosome_length)
    for _ in range(generations):
        next_generation = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            child1, child2 = single_point_crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        population = next_generation
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)

# Example usage
best_solution, best_fitness = genetic_algorithm(
    population_size=100,
    chromosome_length=10,
    generations=100,
    mutation_rate=0.1,
    tournament_size=5
)

print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
