import requests
# print("Hello")
# Define the API endpoint
API_URL = "http://localhost:5000/answer"

# Define a sample query
query_data = {
    "query": "What is this Saclar Course is about?"
}

# Send a POST request to the API
response = requests.post(API_URL, json=query_data)

# Check if the request was successful
if response.status_code == 200:
    # Print the response
    print("Response:", response.json()["answer"])
else:
    # Print error message if request failed
    print("Error:", response.json())
