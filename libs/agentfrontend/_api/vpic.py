import requests
import json

from pydantic import BaseModel

import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from _api import openaichat

def vin_year_extract_mask(text: str, partial: bool = True, mask_only: bool = False) -> tuple:
    """
    Extracts VIN and year from a given text and masks the VIN.
    
    Args:
        text (str): Input text containing VIN and year.
        partial (bool): Whether to return partial VIN (11 digits). Defaults to True.
        mask_only (bool): Whether to return masked text instead of VIN and year. Defaults to False.
    
    Returns:
        tuple or str: A tuple containing the extracted (partial) VIN and year, 
                      or the original text with masked VIN if mask_only is True.
                      Returns (None, None) if not found.
    """
    vin_pattern = re.search(r'\b[A-HJ-NPR-Z0-9]{17}\b', text)
    year_pattern = re.search(r'\b(19|20)\d{2}\b', text)
    
    if vin_pattern and year_pattern:
        vin = vin_pattern.group()
        masked_vin = vin[:8] + '*' + vin[9:11]
        if mask_only:
            return re.sub(vin_pattern.group(), masked_vin, text)
        else:
            return (masked_vin[:11] if partial else vin, year_pattern.group())
    else:
        return None, None
    
def vehicle_details(text:str) -> str:
    """
    Extracts vehicle details from a given text.
    Args:
        text (str): Input text containing VIN and year.
    Returns:
        str: A string containing the vehicle details.
    """
    vin, year = vin_year_extract_mask(text)
    if vin and year:
        client = VpicClient()
        return client.get_vehicle_details_summary(vin, year)
    
    
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
        else:
            return {
                "status_code": response.status_code,
                "status_message": response.reason
            }
    
    def get_vehicle_details_summary(self, vin, year, format="json"):
        response = self.get_short_details_by_vin(vin, year, format)
        return openaichat.vehicle_detail_summary(response)
        

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