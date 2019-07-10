import json
import requests
import os
import logging

api_base_url = "https://api.adoptapet.com/search/pets_at_shelter?key="
api_token = os.environ['ADOPTAPET_API_KEY']
api_version = "v=2"
api_output = "output=json"
api_shelter_id = "shelter_id=79570"

url = api_base_url + api_token + "&" + api_version + \
    "&" + api_output + "&" + api_shelter_id

response = requests.get(url)
if response.status_code != 200:
    logging.Fatal("Could not complete the GET request")
else:
    json_response = json.loads(response.content.decode('utf-8'))
    print("Status: " + json_response['status'])

print("\nPrinting pet names ...\n")

for pet in json_response['pets']:
    name = pet['pet_name']
    id = pet['pet_id']
    print(f'Name: {name}\t ID: {id}')
