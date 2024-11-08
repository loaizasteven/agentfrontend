import requests
import json

class VpicClient:
    def __init__(self):
        self.api_url = "https://vpic.nhtsa.dot.gov/api/"

    # Get details by VIN
    def get_details_by_vin(self, vin, year, format="json"):
        return self.send_request(f"/vehicles/DecodeVinValues/{vin}?format={format}&modelyear={year}")

    # Send a GET request to the vPIC API
    def send_request(self, endpoint):
        url = f"{self.api_url}{endpoint}"
        response = requests.get(url)

        return response


# Usage
if __name__ == "__main__":
    client = VpicClient()

    details = client.get_details_by_vin("5UXWX7C5*BA", 2011)
    if details.status_code == 200:
        print(json.dumps(details.json(), indent=2))