import os
import requests

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

# URL de la nueva Places API (New)
BASE_URL = "https://places.googleapis.com/v1/places:searchText"
