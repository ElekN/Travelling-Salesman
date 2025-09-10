import matplotlib.pyplot as plt

def plot_route(coordinates, path, title="TSP Rešenje"):
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    
    plt.figure(figsize=(10, 8))
    
    plt.scatter(x_coords, y_coords, c='red', s=100)
    for i, txt in enumerate(range(len(coordinates))):
        plt.annotate(txt, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0,10), ha='center')

    for i in range(len(path) - 1):
        start_node = path[i]
        end_node = path[i+1]
        plt.plot(
            [coordinates[start_node][0], coordinates[end_node][0]],
            [coordinates[start_node][1], coordinates[end_node][1]],
            'b-'
        )
        
    plt.title(f"{title}\nstart={path[0]}")
    plt.xlabel("X koordinata")
    plt.ylabel("Y koordinata")
    plt.grid(True)
    plt.show()