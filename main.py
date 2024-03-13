import requests
import os

# load the environment variables
from dotenv import load_dotenv

load_dotenv()

# Replace 'your_salad_api_token' with your actual Salad API Token
salad_api_token = os.getenv("SALAD_API_TOKEN")
# The URL for the Salad API
url = os.getenv("SALAD_API_URL")

headers = {"Salad-Api-Key": salad_api_token, "Content-Type": "application/json"}

# print(headers)

data = {
    
}
# Send the request to the Salad API
# response = requests.get(url, headers=headers, json=data)

response = requests.get(url, headers=headers, json=data)
# print(response)
# print(response.status_code)
# print(response.json())


# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    print("Response:")

    # Get the list of base64 encoded image data
    print(response.json())

else:
    print("Error:", response.status_code, response.text)
