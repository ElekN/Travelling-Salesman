import itertools

def solve(distance_matrix):
    cities = list(range(len(distance_matrix)))
    start_city = cities[0]
    other_cities = cities[1:]

    shortest_path = []
    min_distance = float('inf')
    
    # Generiši sve moguće rute
    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = 0

        # Izračunaj ukupnu distancu za trenutnu rutu
        for i in range(len(current_path) - 1):
            current_distance += distance_matrix[current_path[i]][current_path[i+1]]

        # Ažuriraj ako je pronađena kraća ruta
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = current_path
    
    return shortest_path, min_distance