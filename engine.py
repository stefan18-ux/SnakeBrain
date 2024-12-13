import random
import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    """
    Checks is a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_strategy(grid_width, grid_height, commands):
    """Simulates the snake's movements on a grid and checks coverage."""
    total_cells = grid_width * grid_height
    visited = set()  # Set to track visited cells
    x, y = 0, 0  # Start position
    visited.add((x, y))
    
    moves = {
        'D': (0, 1),
        'R': (1, 0)
    }
    
    steps = 0  # Total steps taken
    for command in commands:
        dx, dy = moves.get(command, (0, 0))
        x = (x + dx) % grid_width
        y = (y + dy) % grid_height
        visited.add((x, y))
        steps += 1
        
        if len(visited) == total_cells:  # All cells visited
            return True, steps
    
    return False, steps

def generate_areas(min_area, max_area, num_areas):
    """Generate a list of evenly spaced areas between min_area and max_area."""
    return [int(area) for area in range(min_area, max_area + 1, max(1, (max_area - min_area) // num_areas))]

def evaluate_strategy(areas, commands, num_tests=100):
    """Test the strategy on multiple grid areas."""
    performance_data = []
    
    for area in areas:
        avg_steps = []
        max_steps = []
        
        # Simulate once for each area
        for _ in range(num_tests):
            # Randomly generate more balanced grid dimensions
            grid_width = random.randint(1, int(area**0.5))
            grid_height = area // grid_width
            
            # Ensure the grid dimensions are at least 1x1
            grid_width = max(grid_width, 1)
            grid_height = max(grid_height, 1)
            
            _, steps = test_strategy(grid_width, grid_height, commands)
            avg_steps.append(steps)  # Collecting steps for average
            max_steps.append(steps)  # Collecting steps for max
        
        # Calculate average and max steps after all tests for each area
        average_steps = sum(avg_steps) / len(avg_steps)  # Calculate average steps
        maximum_steps = max(max_steps)  # Get maximum steps
        
        performance_data.append((area, average_steps, maximum_steps))  # Store results
    
    return performance_data

def plot_performance(performance_data):
    """Plot the performance of the strategy with visual improvements, and save as performance_plot.png."""
    areas = [data[0] for data in performance_data]
    avg_steps = [data[1] for data in performance_data]
    max_steps = [data[2] for data in performance_data]
    limits = [35 * area for area in areas]  # 35*S limit

    plt.figure(figsize=(12, 8))

    # Create scatter plot for Average Steps (blue dots) with transparency and larger points
    plt.scatter(areas, avg_steps, color='royalblue', label='Average Steps', alpha=0.7, s=100, edgecolors='black', linewidth=1.2)

    # Create scatter plot for Maximum Steps (red dots) with transparency and larger points
    plt.scatter(areas, max_steps, color='tomato', label='Maximum Steps', alpha=0.7, s=100, edgecolors='black', linewidth=1.2)

    # Plot y = 35*S (green line) with dashed style for better distinction
    plt.plot(areas, limits, color='forestgreen', label='y = 35*S', linestyle='--', linewidth=3)

    # Optional: Adding a trendline (linear regression) for Average Steps
    z = np.polyfit(areas, avg_steps, 1)
    p = np.poly1d(z)
    plt.plot(areas, p(areas), color='dodgerblue', linestyle='-', linewidth=2, label='Trendline (Avg Steps)')

    # Titles and labels
    plt.title('Number of Steps to Cover the Grid vs Grid Area', fontsize=16)
    plt.xlabel('Grid Area (number of cells)', fontsize=14)
    plt.ylabel('Number of Steps Taken', fontsize=14)

    # Customize grid and axes
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
    plt.xscale('log')  # Logarithmic scale for X-axis (if needed)
    plt.yscale('log')  # Logarithmic scale for Y-axis (if needed)

    # Add a legend with a more readable font size
    plt.legend(fontsize=12)

    # Tight layout to avoid overlap
    plt.tight_layout()

    # Save the plot to the file 'performance_plot.png'
    plt.savefig("performance_plot.png")
    print("Plot saved as 'performance_plot.png'.")

    # Optionally, show the plot in the interactive window
    plt.show()  # Show plot in the interactive window