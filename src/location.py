import requests
import json

def load_api_key():
    with open("api_keys.json", 'r') as f:
        data = json.load(f)
        return data["google"]


def elevation(longitude,latitude):
    """
    Returns the elevation above sea level (in meters), using the google elevation api
    """
    key = load_api_key()
    elevation_url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={longitude}%2C{latitude}&key={key}"

    payload={}
    headers = {}

    response = requests.request("GET", elevation_url, headers=headers, data=payload)
    response_json = response.json()
    response_status = response_json["status"]
    if response_status!="OK":
        print(f"Error while getting request : {response_status}")
        return None 
    if len(response_json["results"])==0:
        print("Error : Result size is 0")
        return None
    return response_json["results"][0]["elevation"]

