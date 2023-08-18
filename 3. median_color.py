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

all_colors = [color for _, colors in data for color in colors]

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
inverse_color_mapping = {v: k for k, v in color_mapping.items()}
median_color = inverse_color_mapping[round(median_numerical_color)]

print("The median color worn throughout the week:", median_color)