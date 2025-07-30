def solve(distance_matrix):
    num_cities = len(distance_matrix)
    unvisited = list(range(num_cities))
    start_city = 0
    path = [start_city]
    unvisited.remove(start_city)
    current_city = start_city
    total_distance = 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_distance += distance_matrix[current_city][nearest_city]
        current_city = nearest_city
        path.append(current_city)
        unvisited.remove(current_city)

    # Vraćanje u početni grad
    total_distance += distance_matrix[current_city][start_city]
    path.append(start_city)

    return path, total_distance