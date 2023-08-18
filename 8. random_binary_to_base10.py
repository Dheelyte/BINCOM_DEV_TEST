import random

# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print("Generated Binary Number:", binary_number)
print("Decimal Equivalent:", decimal_number)