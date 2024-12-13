from engine import *

def main():
    # Generating the first 200 prime numbers, i think that's gonna be enough for any dimesnion we may get
    count = 0
    number = 2
    primes = []
    commands = []

    while count < 200:
        if is_prime(number):
            primes.append(number)
            count += 1
        number += 1


    max_moves = 35 * 10**6
    moves = 0
    ending_index = 14

    while (moves < max_moves):
        ending_index *= 2
        
        if ending_index > len(primes):
            ending_index = 14

        numbers = primes[0:ending_index]

        for num in numbers:
            
            for i in range(num):
                if moves >= max_moves:
                    break
                commands.append("R\n")
                moves += 1

            if moves >= max_moves:
                break

            if moves < max_moves:
                commands.append("D\n")
                moves += 1
            

        if moves >= max_moves:
            break

    """Run multiple simulations and visualize results."""
    print("Enter the range of grid areas:")
    min_area = int(input("Minimum area: "))
    max_area = int(input("Maximum area: "))
    num_areas = int(input("Number of areas to test: "))
    num_tests_per_area = int(input("Number of simulations per area: "))
    
    areas = generate_areas(min_area, max_area, num_areas)
    print(f"Generated areas: {areas}")
    
    performance_data = evaluate_strategy(areas, commands, num_tests_per_area)
    
    print("\nPerformance Summary:")
    for area, avg_steps, max_steps in performance_data:
        print(f"Area {area}: Avg Steps = {avg_steps:.2f}, Max Steps = {max_steps}")
    
    plot_performance(performance_data)

if __name__ == '__main__':
    main()
