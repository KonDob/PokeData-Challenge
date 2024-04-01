import matplotlib.pyplot as plt
from db_operations import PokemonDatabase, pokemon_db_name


with PokemonDatabase(pokemon_db_name) as db:
    # Gets results
    rows = db.execute_query("SELECT height, weight FROM pokemon_data")


# Split data about high and weight of each pokemon
heights = [row[0] for row in rows]
weights = [row[1] for row in rows]
bmis = [(row[1] / (row[0] ** 2)) for row in rows]

# Create a graphical window with two subgraphs
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Create a scatterplot for Pokemon's height and weight
ax1.scatter(heights, weights, alpha=0.5)
ax1.set_title('Relationship between Height and Weight of Pokémon')
ax1.set_xlabel('Height')
ax1.set_ylabel('Weight')
ax1.grid(True)

# Creation of histogram BMI value
ax2.hist(bmis, bins=20, color='skyblue', edgecolor='black')
ax2.set_title('Histogram of BMI Values of Pokémon')
ax2.set_xlabel('BMI')
ax2.set_ylabel('Frequency')
ax2.grid(True)

# Show plots together
plt.tight_layout()
plt.show()
