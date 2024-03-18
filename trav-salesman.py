import random
import numpy as np
import matplotlib.pyplot as plt

# Define the cities (coordinates)
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 1),
    'D': (3, 5),
    'E': (4, 2),
    'F': (5, 0)
}

# Define the distance function (Euclidean distance)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize parameters
num_cities = len(cities)
population_size = 50
num_generations = 1000
mutation_rate = 0.1
tournament_size = 3
elite_size = 2

# Generate initial population
def generate_random_route():
    cities_list = list(cities.keys())
    random.shuffle(cities_list)
    return cities_list

population = [generate_random_route() for _ in range(population_size)]

# Calculate route distance (fitness)
def route_distance(route):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distance(route[i], route[i + 1])
    total_distance += distance(route[-1], route[0])  # Return to the starting city
    return total_distance

# Genetic Algorithm loop
best_fitness_values = []
for generation in range(num_generations):
    # Evaluate fitness
    fitness_scores = [1 / route_distance(route) for route in population]
    best_fitness = max(fitness_scores)
    best_fitness_values.append(1 / best_fitness)

    # Select parents using tournament selection
    parents = []
    for _ in range(population_size):
        tournament = random.sample(list(enumerate(fitness_scores)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        parents.append(population[winner])

    # Perform crossover (order crossover)
    offspring = []
    for i in range(0, population_size, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        crossover_point1 = random.randint(0, num_cities - 2)
        crossover_point2 = random.randint(crossover_point1 + 1, num_cities - 1)
        child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
        child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
        offspring.extend([child1, child2])

    # Mutate offspring (swap mutation)
    for i in range(population_size):
        if random.random() < mutation_rate:
            mutate_index1 = random.randint(0, num_cities - 1)
            mutate_index2 = random.randint(0, num_cities - 1)
            offspring[i][mutate_index1], offspring[i][mutate_index2] = offspring[i][mutate_index2], offspring[i][mutate_index1]

    # Elitism: Select the best individuals to survive
    population_with_fitness = list(zip(population, fitness_scores))
    sorted_population = sorted(population_with_fitness, key=lambda x: x[1], reverse=True)
    elite_population = [ind for ind, _ in sorted_population[:elite_size]]
    population = elite_population + offspring[:population_size - elite_size]

# Get the best route (solution)
best_route = min(population, key=route_distance)
best_route_distance = route_distance(best_route)

print("Best Route:", best_route)
print("Best Route Distance:", best_route_distance)

# Plotting the fitness progress
plt.figure(figsize=(8, 6))
plt.plot(best_fitness_values)
plt.title('Fitness Progress')
plt.xlabel('Generation')
plt.ylabel('Fitness (1/Distance)')
plt.grid(True)
plt.show()
