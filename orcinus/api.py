import requests
from datetime import datetime, timedelta
import json

class Api:
    def __init__(self, save_file='api_data.json') -> None:
        self.save_file = save_file
        self.last_fetch_time = None
        self.cached_data = None

    def save_data(self, data):
        with open(self.save_file, 'w') as file:
            json.dump({'data': data, 'timestamp': datetime.now().isoformat()}, file)

    def load_data(self):
        try:
            with open(self.save_file, 'r') as file:
                saved_data = json.load(file)
                self.cached_data = saved_data['data']
                self.last_fetch_time = datetime.fromisoformat(saved_data['timestamp'])
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def connect_to_api(self, url):
        try:
            # Load cached data
            self.load_data()
            
            # Check if it's been more than 15 minutes since the last fetch
            if self.last_fetch_time is None or datetime.now() - self.last_fetch_time > timedelta(minutes=15):
                print("fetching data")
                response = requests.get(url)
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Update the last fetch time
                    self.last_fetch_time = datetime.now()
                    # Save the JSON data
                    self.save_data(response.json())
                    # Return the JSON data retrieved from the API
                    return response.json()
                else:
                    # If the request was not successful, print the error status code
                    print(f"Failed to connect. Status code: {response.status_code}")
                    return self.cached_data  # Return cached data if available
            else:
                print("Data fetched within the last 15 minutes. Returning cached data.")
                return self.cached_data  # Return cached data if available
        except Exception as e:
            # Print any exception that occurred during the request
            print(f"An error occurred: {str(e)}")
            return self.cached_data  # Return cached data if available
