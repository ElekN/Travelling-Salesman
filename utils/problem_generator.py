import numpy as np
import math

def calculate_distance_matrix(coordinates):
    num_cities = len(coordinates)
    
    dist_matrix = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i == j:
                continue
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            dist_matrix[i, j] = distance
            
    return dist_matrix

def generate_problem(num_cities, min_coord=0, max_coord=100, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
    coordinates = np.random.randint(min_coord, max_coord + 1, size=(num_cities, 2))
    
    distance_matrix = calculate_distance_matrix(coordinates)
    
    return coordinates, distance_matrix
