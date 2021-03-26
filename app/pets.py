import json
import requests
import os


def get_pets():
    api_base_url = "https://api.adoptapet.com/search/pets_at_shelters?v=2&output=json&shelter_id=77070&shelter_id=79568&shelter_id=79570&shelter_id=99754&shelter_id=79569&shelter_id=80090&key="
    # api_key = os.environ['ADOPTAPET_API_KEY']
    api_key = '54188660446c78dd431e966d72efbf86' # temp

    url = api_base_url + api_key

    response = requests.get(url)
    if response.status_code != 200:
        print("Could not complete GET request")
        return
    else:
        json_response = json.loads(response.content.decode('utf-8'))

    all_pets = {}
    all_pets['Austin'] = []
    all_pets['SanAntonio'] = []
    all_pets['DallasFtWorth'] = []
    all_pets['Houston'] = []
    all_pets['OKC'] = []
    all_pets['Louisiana'] = []

    for pet in json_response['pets']:
        if pet['addr_city'] == 'Austin':
            all_pets['Austin'].append(pet)
        elif pet['addr_city'] == 'Dallas/Ft. Worth':
            all_pets['DallasFtWorth'].append(pet)
        elif pet['addr_city'] == 'Houston':
            all_pets['Houston'].append(pet)
        elif pet['addr_city'] == 'Oklahoma City':
            all_pets['OKC'].append(pet)
        elif pet['addr_city'] == 'San Antonio':
            all_pets['SanAntonio'].append(pet)
        elif pet['addr_city'] == 'Louisiana':
            all_pets['Louisiana'].append(pet)
        else:
            print("Error")

    return all_pets


def pet_get_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Could not complete GET request")
        return
    else:
        json_response = json.loads(response.content.decode('utf-8'))

    return json_response


def get_all_pets():
    owner_surrender_base_url = "https://api.adoptapet.com/search/pets_at_shelters?v=2&output=json&shelter_id=77070&key="
    rescue_base_url = "https://api.adoptapet.com/search/pets_at_shelters?v=2&output=json&shelter_id=79568&shelter_id=79570&shelter_id=99754&shelter_id=79569&shelter_id=80090&key="
    # api_key = os.environ['ADOPTAPET_API_KEY']
    api_key = '54188660446c78dd431e966d72efbf86' # temp

    owner_url = owner_surrender_base_url + api_key
    rescue_url = rescue_base_url + api_key

    # two GET requests bc there is no shelter_id reference in responses
    owner_pets = pet_get_request(owner_url)
    rescue_pets = pet_get_request(rescue_url)

    all_pets = []

    for pet in rescue_pets['pets']:
        all_pets.append(pet)

    for pet in owner_pets['pets']:
        # add a k/v that indicates this is an owner surrender pet
        pet['ownerSurrender'] = True
        all_pets.append(pet)

    # return the dogs by alphabetization in ascending alphabetical order
    return sorted(all_pets, key = lambda i: i['pet_name'])


if __name__ == "__main__":
    a = get_all_pets()
