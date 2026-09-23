import json
import requests

# Define the URL of your Spring Boot API endpoint
requestCategory = "readCSV?category=InterestRate"
#requestCategory = "country/allcountries"
url = "http://localhost:8080/"+requestCategory  # Replace with your actual endpoint

# Define request parameters or data (if needed)
params = {"param1": "value1"}
data = {"key": "value"}

# Make a GET request
response = requests.get(url)

# Make a POST request
#response = requests.post(url, json=data)

# Check the response status and content
if response.status_code == 200:
    print("Success!")
    print(response.text)
else:
    print(f"Error: {response.status_code}")
    print(response.text)