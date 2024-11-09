# VIN Decoding API Documentation

## Introduction
The VIN Decoding API provided by the National Highway Traffic Safety Administration (NHTSA) allows users to decode Vehicle Identification Numbers (VINs) and retrieve detailed information about vehicles.

## API Endpoint
The API endpoint for VIN decoding is `https://vpic.nhtsa.dot.gov/api//vehicles/DecodeVinValues/{vin}?format={format}&modelyear={year}`. Replace `{vin}` with the VIN and `{year}` with model year you want to decode.

## Request Parameters
The VIN Decoding API requires the following request parameter:

- `vin` (string): The Vehicle Identification Number to be decoded.

## Response
The API response will be in JSON format and will contain detailed information about the vehicle associated with the provided VIN. The response may include the following fields:

- `Make`: The make of the vehicle.
- `Model`: The model of the vehicle.
- `Year`: The manufacturing year of the vehicle.
- `BodyClass`: The body class of the vehicle.
- `EngineCylinders`: The number of cylinders in the vehicle's engine.
- `FuelTypePrimary`: The primary fuel type of the vehicle.
- `TransmissionStyle`: The transmission style of the vehicle.
- `DriveType`: The drive type of the vehicle.
- `PlantCity`: The city where the vehicle was manufactured.

## Python Client
The directory contains a [Python Client](./vpic.py) to interact with the NHTSA api and provide a parsed response.

Sample Response:

{
    "Make": "Honda",
    "Model": "Accord",
    "Year": 2003,
    "BodyClass": "Sedan",
    "EngineCylinders": 6,
    "FuelTypePrimary": "Gasoline",
    "TransmissionStyle": "Automatic",
    "DriveType": "FWD",
    "PlantCity": "Marysville"
}

For more information, please refer to the [official documentation](https://vpic.nhtsa.dot.gov/api/).
