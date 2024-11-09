import requests
import json

from pydantic import BaseModel

class VpicClient(BaseModel):
    api_url: str = "https://vpic.nhtsa.dot.gov/api/"

    # Get details by VIN
    def get_details_by_vin(self, vin, year, format="json"):
        return self.send_request(f"/vehicles/DecodeVinValues/{vin}?format={format}&modelyear={year}")

    def get_short_details_by_vin(self, vin, year, format="json"):
        response = self.get_details_by_vin(vin, year, format)
        if response.status_code == 200:
            data = response.json()
            if "Results" in data:
                results = data["Results"][0]
                return {
                    "apiMessage": data["Message"],
                    "make": results["Make"],
                    "model": results["Model"],
                    "year": results["ModelYear"],
                    "gvwr": results["GVWR"],
                    "basePrice": results["BasePrice"]
                }

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