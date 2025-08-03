import numpy as np

def generate(num_cities, min_dist=10, max_dist=100, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
    matrix = np.random.randint(min_dist, max_dist + 1, size=(num_cities, num_cities))
    symmetric_matrix = (matrix + matrix.T) // 2   
    np.fill_diagonal(symmetric_matrix, 0)
    
    return symmetric_matrix