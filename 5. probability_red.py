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

all_colors = [color for _, colors in data for color in colors]

color_counts = Counter(all_colors)

# Calculate the probability of choosing red
probability_red = color_counts["RED"] / len(all_colors)

print("Probability of choosing RED:", probability_red)