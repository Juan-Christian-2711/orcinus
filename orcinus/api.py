import requests  
class Api:
    def __init__(self) -> None:
        pass
    def connect_to_api(self, url):     
        try:         
            response = requests.get(url)         
            # Check if the request was successful (status code 200)         
            if response.status_code == 200:             
                # Return the JSON data retrieved from the API             
                return response.json()         
            else:             
                # If the request was not successful, print the error status code             
                print(f"Failed to connect. Status code: {response.status_code}")             
                return None     
        except Exception as e:         
                # Print any exception that occurred during the request         
                print(f"An error occurred: {str(e)}")         
                return None  
