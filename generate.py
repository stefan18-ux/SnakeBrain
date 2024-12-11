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


with open("file.txt", 'w') as f:
        f.write(''.join(commands))
