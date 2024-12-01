import requests
from flask import abort
from config import load_config
envConfig = load_config()

def get_service_data():   
    
    try:
        response = requests.get(envConfig.url)
        response.raise_for_status()  # Will raise an exception for HTTP errors (4xx, 5xx)
        
        # Parse and return the JSON response
        return response.json()
    
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
        abort(500, description=f"HTTP error occurred: {errh}")
        
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
        abort(500, description=f"HTTP error occurred: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
        abort(500, description=f"HTTP error occurred: {errh}")

    return None  # Return None if there is an error


