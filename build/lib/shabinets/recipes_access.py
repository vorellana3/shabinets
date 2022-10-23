import json
import requests


response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q=bacon&app_id=93598680&app_key=c8eaae5039730056d24a50c29c448761")
response = response.json()
print(response["hits"][0])

