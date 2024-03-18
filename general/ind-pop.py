import random

def create_individual(chromosome_length):
    return [random.randint(0, 1) for _ in range(chromosome_length)]

def create_population(population_size, chromosome_length):
    return [create_individual(chromosome_length) for _ in range(population_size)]
