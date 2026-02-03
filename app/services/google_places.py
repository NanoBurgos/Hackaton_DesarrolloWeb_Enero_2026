import os
import requests

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

# URL de la nueva Places API (New)
BASE_URL = "https://places.googleapis.com/v1/places:searchText"

def buscar_negocios(query):
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_PLACES_API_KEY,
        "X-Goog-FieldMask": (
            "places.displayName,"
            "places.formattedAddress,"
            "places.websiteUri,"
            "places.types,"
            "places.rating,"
            "places.location"
        )
    }

    payload = {
        "textQuery": query,
        "languageCode": "es"
    }

    print(f"DEBUG: Llamando a Places API V1 para: {query}")
    response = requests.post(BASE_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"DEBUG: Error Error API: {response.status_code} - {response.text}")
        return []

    data = response.json()
    results = data.get("places", [])
    print(f"DEBUG: API V1 devolvió {len(results)} resultados")
    
    return results
