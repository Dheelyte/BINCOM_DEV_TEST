from collections import Counter

# Sample data
data = [
    ("Monday", ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE",
                "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM",
                "ORANGE", "RED", "WHITE", "BLUE", "WHITE",
                "BLUE", "BLUE", "BLUE", "GREEN"]),
    ("Tuesday", ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE",
                 "BLUE", "BLEW", "PINK", "PINK", "ORANGE",
                 "ORANGE", "RED", "WHITE", "BLUE", "WHITE",
                 "WHITE", "BLUE", "BLUE", "BLUE"]),
    ("Wednesday", ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE",
                   "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE",
                   "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE",
                   "WHITE", "WHITE"]),
    ("Thursday", ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN",
                  "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED",
                  "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]),
    ("Friday", ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK",
                "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE",
                "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"])
]

# Color mapping
color_mapping = {
    "GREEN": 1,
    "YELLOW": 2,
    "BROWN": 3,
    "BLUE": 4,
    "PINK": 5,
    "ORANGE": 6,
    "CREAM": 7,
    "RED": 8,
    "WHITE": 9,
    "ARSH": 10,
    "BLACK": 11,
    "BLEW": 12
}

# Convert colors to numerical values and calculate the total
total_numerical_color = 0
total_color_count = 0

for _, colors in data:
    for color in colors:
        total_numerical_color += color_mapping[color]
        total_color_count += 1

# Calculate the mean numerical color value
mean_numerical_color = total_numerical_color / total_color_count

# Convert the mean numerical color value back to its corresponding color
inverse_color_mapping = {v: k for k, v in color_mapping.items()}
mean_color = inverse_color_mapping[round(mean_numerical_color)]

print("Mean color of all days:", mean_color)

# Flatten the list of colors for all days
all_colors = [color for _, colors in data for color in colors]

# Count the occurrences of each color
color_counts = Counter(all_colors)

# Find the color with the highest occurrence count
most_worn_color = color_counts.most_common(1)[0][0]

print("The color mostly worn throughout the week:", most_worn_color)

# Convert colors to numerical values
numerical_colors = [color_mapping[color] for color in all_colors]

# Sort the numerical colors
sorted_numerical_colors = sorted(numerical_colors)

# Calculate the median index
num_colors = len(sorted_numerical_colors)
median_index = num_colors // 2

if num_colors % 2 == 1:
    median_numerical_color = sorted_numerical_colors[median_index]
else:
    median_numerical_color = (sorted_numerical_colors[median_index - 1] + sorted_numerical_colors[median_index]) / 2

# Convert the median numerical color value back to its corresponding color
median_color = inverse_color_mapping[round(median_numerical_color)]

print("The median color worn throughout the week:", median_color)


numerical_colors = [color_mapping[color] for color in all_colors]

# Calculate the mean color (as a numerical value)
mean_color = sum(numerical_colors) / len(numerical_colors)

# Calculate the squared differences between each color and the mean color
squared_diffs = [(color - mean_color) ** 2 for color in numerical_colors]

# Calculate the mean of the squared differences (variance)
variance = sum(squared_diffs) / len(squared_diffs)

print("Variance of the colors:", variance)


# Calculate the probability of choosing red
probability_red = color_counts["RED"] / len(all_colors)

print("Probability of choosing RED:", probability_red)



def binary_search_recursive(arr, target, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example list of numbers (sorted)
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Get input from the user
target_number = int(input("Enter the number you want to search for: "))

# Call the recursive search function
found = binary_search_recursive(numbers, target_number, 0, len(numbers) - 1)

if found:
    print("Number found in the list.")
else:
    print("Number not found in the list.")



import random

# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print("Generated Binary Number:", binary_number)
print("Decimal Equivalent:", decimal_number)



def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return sum(fib_sequence)

num_terms = 50
fibonacci_sum_50 = fibonacci_sum(num_terms)
print("Sum of the first", num_terms, "Fibonacci terms:", fibonacci_sum_50)

