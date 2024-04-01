import sqlite3


class PokemonDatabase:
    def __init__(self, database_name):
        self.database_name = database_name

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.database_name)
            self.cursor = self.conn.cursor()
            return self
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon_data (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    height REAL,
                                    weight REAL,
                                    bmi REAL
                                )''')
            self.conn.commit()
            print("Table 'pokemon_data' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def load_data_into_table(self, data):
        try:
            for row in data:
                self.cursor.execute('''INSERT OR REPLACE INTO pokemon_data (id, name, height, weight, bmi)
                                      VALUES (?, ?, ?, ?, ?)''',
                                     (row['id'], row['name'], row['height'], row['weight'], row['bmi']))
            self.conn.commit()
            print("Data loaded into the 'pokemon_data' table successfully.")
        except sqlite3.Error as e:
            print(f"Error loading data into table: {e}")

    def max_bmi(self):
        try:
            self.cursor.execute("SELECT MAX(bmi) FROM pokemon_data")
            max_value = round(self.cursor.fetchone()[0], 2)
            print("Max BMI:", max_value)
            return max_value
        except sqlite3.Error as e:
            print(f"Error getting max BMI: {e}")

    def average_bmi(self):
        try:
            self.cursor.execute("SELECT AVG(bmi) FROM pokemon_data")
            avg_value = round(self.cursor.fetchone()[0], 2)
            print("Average BMI:", avg_value)
            return avg_value
        except sqlite3.Error as e:
            print(f"Error getting average BMI: {e}")


pokemon_db_name = 'pokemon.db'

with PokemonDatabase(pokemon_db_name) as db:
    db.create_table()
    db.average_bmi()
    db.max_bmi()
