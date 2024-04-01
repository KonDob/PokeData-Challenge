import csv
import requests
import logging

# Logger configuration
logging.basicConfig(level=logging.INFO)  # INFO level allow to show only informational messages


def fetch_pokemon_data(url):
    """ Gets data from provided URL.
    Return JSON object if success, None otherwise."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None


def process_pokemon_data(pokemon_data) -> dict or None:
    """
    Return processed data about pokemon, otherwise None
    """
    if not pokemon_data:
        return None
    processed_data = {
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
    }
    return processed_data


def main():

    # URL configs
    api_url = "https://pokeapi.co/api/"
    api_version = "v2/"
    ability_endpoint = "pokemon/"
    target_url = f"{api_url}{api_version}{ability_endpoint}?limit=50"
    result_file_name = "pokemons.csv"

    # Getting data about pokemons
    data = fetch_pokemon_data(target_url)
    if not data:
        logging.error("No data retrieved. Exiting.")
        return

    # Processing pokemons data
    all_processed_data = []
    for i in data.get('results', []):
        pokemon_data = fetch_pokemon_data(i['url'])
        processed_data = process_pokemon_data(pokemon_data)
        if processed_data:
            all_processed_data.append(processed_data)

    # Writing data to CSV file
    if all_processed_data:
        with open(result_file_name, 'w', newline='') as csv_file:
            fieldnames = ['id', 'name', 'height', 'weight']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for pokemon in all_processed_data:
                print(pokemon)
                writer.writerow(pokemon)
        logging.info(f"Data successfully written to {result_file_name}")
    else:
        logging.info("No data to write to CSV.")


if __name__ == "__main__":
    main()
