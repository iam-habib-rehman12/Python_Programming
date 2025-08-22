# Connecting to API
import requests

base_url="https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code==200:
        pokemon_data=response.json()
        # print("Data retrieved")
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None


pokemon_name="Typhlosion"      # Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Pikachu
pokemon_info=get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")