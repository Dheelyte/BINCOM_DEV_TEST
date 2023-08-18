import psycopg2

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

color_frequency = {}

for _, colors in data:
    for color in colors:
        if color in color_frequency:
            color_frequency[color] += 1
        else:
            color_frequency[color] = 1

print(color_frequency)


# Database connection details
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'  # Change the port if necessary
}

# Connect to the PostgreSQL database
connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

# Create a table to store colors and frequencies
create_table_query = '''
    CREATE TABLE color_frequencies (
        color_name VARCHAR(255) PRIMARY KEY,
        frequency INTEGER
    )
'''
cursor.execute(create_table_query)

# Insert data into the table
for color, frequency in color_frequency.items():
    insert_query = '''
        INSERT INTO color_frequencies (color_name, frequency)
        VALUES (%s, %s)
    '''
    cursor.execute(insert_query, (color, frequency))

# Commit changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted into the database.")
