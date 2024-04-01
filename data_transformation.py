import apache_beam as beam
import pandas as pd
from db_operations_new import PokemonDatabase
import logging

# Logger configuration
logging.basicConfig(level=logging.INFO)  # INFO level allow to show only informational messages


def convert_units(row):
    pokemon = {
        'id': int(row['id']),
        'name': row['name'],
        'height': round(float(row['height']) * 0.1, 2),  # Convert height from decimetres to metres
        'weight': round(float(row['weight']) * 0.1, 2)  # Convert weight from hectograms to kilograms
    }
    height_m = pokemon['height']
    weight_kg = pokemon['weight']
    bmi = round(weight_kg / (height_m ** 2), 2)  # Calculate BMI and round to two decimal places
    pokemon['bmi'] = bmi
    return pokemon


def format_csv(row):
    return f"{row['id']},{row['name']},{row['height']},{row['weight']},{row['bmi']}"


def load_data(row):
    # Init DB connection
    database_name = 'pokemon.db'
    db = PokemonDatabase(database_name)
    # Apply the function of loading data into the table to each element of the PCollection
    with PokemonDatabase(database_name) as db:
        db.load_data_into_table([row])
    return []


# Function to print items
def log_transformed_items(pokemon_list):
    for pokemon in pokemon_list:
        logging.info(pokemon)


# Main data pipeline
with beam.Pipeline() as pipeline:

    # Read data from CSV file using pandas
    df = pd.read_csv('pokemons.csv')

    # Convert pandas DataFrame to PCollection
    pcoll = pipeline | beam.Create(df.to_dict('records'))

    # Apply the conversion function to each record
    transformed_pokemon = pcoll | 'Convert Units' >> beam.Map(convert_units)

    # Format the data as CSV strings
    formatted_csv = transformed_pokemon | 'Format as CSV' >> beam.Map(format_csv)

    # Write the transformed data to a CSV file
    formatted_csv | 'Write Transformed Pokemon Data' >> beam.io.WriteToText(
        file_path_prefix='transformed_pokemon_data', file_name_suffix='.csv', header=None, coder=str,
        num_shards=1)

    # Save transformed data in BD
    transformed_pokemon | 'Insert into Database' >> beam.Map(load_data)

    # Collect transformed items into a list
    transformed_pokemon_list = (transformed_pokemon | 'Collect Transformed Pokemon' >> beam.combiners.ToList())

    transformed_pokemon_list | 'Log Transformed Pokemon' >> beam.Map(log_transformed_items)
