import random

def solve(distance_matrix, population_size=50, generations=200, mutation_rate=0.01):
    num_cities = len(distance_matrix)

    # Kreiranje jedne rute (individuuma)
    def create_route():
        route = list(range(num_cities))
        random.shuffle(route)
        return route

    # Računanje distance (inverzna vrednost za fitness)
    def calculate_distance(route):
        distance = 0
        for i in range(num_cities):
            distance += distance_matrix[route[i]][route[i-1]] # Koristi i-1 za povratak na početak
        return distance

    # Selekcija roditelja (Tournament selection)
    def selection(population, fitnesses):
        tournament = random.sample(list(zip(population, fitnesses)), k=5)
        tournament.sort(key=lambda x: x[1]) # Sortira po fitness-u (niža distanca je bolja)
        return tournament[0][0]

    # Ukrštanje (Ordered Crossover)
    def crossover(parent1, parent2):
        child = [None] * num_cities
        start, end = sorted(random.sample(range(num_cities), 2))
        child[start:end] = parent1[start:end]
        
        pointer = 0
        for i in range(num_cities):
            if child[i] is None:
                while parent2[pointer] in child:
                    pointer += 1
                child[i] = parent2[pointer]
        return child

    # Mutacija (Swap Mutation)
    def mutate(route, mutation_rate):
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(num_cities), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]
        return route

    # Inicijalizacija populacije
    population = [create_route() for _ in range(population_size)]

    best_route_ever = None
    best_distance_ever = float('inf')

    # Glavna petlja genetskog algoritma
    for _ in range(generations):
        fitnesses = [calculate_distance(route) for route in population]

        for i in range(population_size):
            if fitnesses[i] < best_distance_ever:
                best_distance_ever = fitnesses[i]
                best_route_ever = population[i]

        new_population = []
        for _ in range(population_size):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            new_population.append(mutate(child, mutation_rate))
        population = new_population

    best_route_ever.append(best_route_ever[0]) # Dodaj početni grad na kraj za prikaz
    
    return best_route_ever, best_distance_ever