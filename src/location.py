import requests
import json



def elevation(longitude,latitude):
    """
    Returns the elevation above sea level (in meters), using the google elevation api
    """
    elevation_url = f"https://api.open-elevation.com/api/v1/lookup?locations={longitude},{latitude}"
    payload={}
    headers = {}

    response = requests.request("GET", elevation_url, headers=headers, data=payload)
    response_json = response.json()
    if not response.ok:
        print(f"Error while getting request : {response_status}")
        return None 
    if len(response_json["results"])==0:
        print("Error : Result size is 0")
        return None
    return response_json["results"][0]["elevation"]

