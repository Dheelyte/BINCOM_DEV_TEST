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

# Flatten the list of colors for all days
all_colors = [color for _, colors in data for color in colors]

numerical_colors = [color_mapping[color] for color in all_colors]

# Calculate the mean color (as a numerical value)
mean_color = sum(numerical_colors) / len(numerical_colors)

# Calculate the squared differences between each color and the mean color
squared_diffs = [(color - mean_color) ** 2 for color in numerical_colors]

# Calculate the mean of the squared differences (variance)
variance = sum(squared_diffs) / len(squared_diffs)

print("Variance of the colors:", variance)