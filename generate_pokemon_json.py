import requests
import json

URL = "https://pokeapi.co/api/v2/pokemon-species"
OUTPUT_FILE = "pokemon_species.json"
REQUEST_LIMIT = 100000

def generate_pokemon_json():
    response = requests.get(URL, params={'limit': REQUEST_LIMIT})
    response.raise_for_status()
    
    data = response.json()
    pokemon_names = [pokemon["name"] for pokemon in data["results"]]
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(pokemon_names, f, indent=2)

    print(f"Saved {len(pokemon_names)} Pokémon names to {OUTPUT_FILE}")

if __name__ == '__main__':
    generate_pokemon_json()