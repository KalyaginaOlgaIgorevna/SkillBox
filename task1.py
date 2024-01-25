import requests
import json

def fetch_star_wars_data():
    base_url = "https://swapi.dev/api"

    def fetch_character_details(url):
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    starships_response = requests.get(f"{base_url}/starships/")
    starships = starships_response.json().get("results", [])
    millennium_falcon = next((ship for ship in starships if ship["name"] == "Millennium Falcon"), None)

    if not millennium_falcon:
        return "Millennium Falcon not found in API data."

    pilots_info = []
    for pilot_url in millennium_falcon.get("pilots", []):
        pilot = fetch_character_details(pilot_url)
        if pilot:
            home_world = fetch_character_details(pilot["homeworld"]) if pilot["homeworld"] else None
            pilots_info.append({
                "name": pilot["name"],
                "height": pilot["height"],
                "mass": pilot["mass"],
                "homeworld": home_world["name"] if home_world else "Unknown",
                "homeworld_url": pilot["homeworld"]
            })

    millennium_falcon_data = {
        "name": millennium_falcon["name"],
        "max_speed": millennium_falcon["max_atmosphering_speed"],
        "class": millennium_falcon["starship_class"],
        "pilots": pilots_info
    }

    return millennium_falcon_data

millennium_falcon_data = fetch_star_wars_data()

# Вывод информации на экран и сохранение в JSON-файл
print(millennium_falcon_data)
with open('millennium_falcon_data.json', 'w') as file:
    json.dump(millennium_falcon_data, file, indent=4)

