import heapq

def solve(distance_matrix):
    if len(distance_matrix) >= 13:
        print("Broj gradova prevelik za brute force")
        return [], 0

    num_cities = len(distance_matrix)
    
    pq = [(0, [0])] 
    
    min_distance = float('inf')
    best_path = []
    
    while pq:
        current_cost, current_path = heapq.heappop(pq)
        
        if current_cost >= min_distance:
            continue
            
        last_city = current_path[-1]
        
        if len(current_path) == num_cities:
            final_cost = current_cost + distance_matrix[last_city][0]
            
            if final_cost < min_distance:
                min_distance = final_cost
                best_path = current_path + [0]
            continue

        for next_city in range(num_cities):
            if next_city not in current_path:
                new_cost = current_cost + distance_matrix[last_city][next_city]
                
                if new_cost < min_distance:
                    new_path = current_path + [next_city]
                    heapq.heappush(pq, (new_cost, new_path))
                    
    return best_path, min_distance