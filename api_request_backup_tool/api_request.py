import requests
import json

# Base API Application

BASE_URL = "https://jsonplaceholder.typicode.com"
RESOURCE = "posts"
TIMEOUT = 5

# Accept user input and validation
while True:
	try:
		post_id = int(input("Enter post ID (1 - 100): ").strip())

		if 1 <= post_id <= 100:
			break

		else:
			print("Error: Post ID must be between 1 and 100.")
	except ValueError:
		print("Error: Post ID must be an integer")
	except KeyboardInterrupt:
		print("Input cancelled by user. Exiting program...")
		exit()

# Build API URL
url = f"{BASE_URL}/{RESOURCE}/{post_id}"

# API Request and Parsing
try:
	# Send request to the API with time protection
	response = requests.get(url, timeout = TIMEOUT)

	# Raise an exception if the response contains an HTTP error(e.g., 404, 500)
	response.raise_for_status()

	# Convert JSON response into a Python dictionary
	data = response.json()

	# Print debugging informaton
	print("\n--- DEBUG INFO ---")
	print("Status Code:", response.status_code)
	print("Headers:", json.dumps(dict(response.headers), indent = 4))
	print("Body:", json.dumps(data, indent = 4))

	# Check if the API returned data
	if not data:
		print("Error: The API returned no data.")
		exit()

	# The API returned a single post(dictionary)
	if isinstance(data, dict):
		print(f"\nUser ID : {data.get('userId')}")
		print(f"Post ID : {data.get('id')}")
		print(f"Title   : {data.get('title')}")
		print(f"Body    : {data.get('body')}")

	# The API returned multiple post(list)
	elif isinstance(data, list):

		# Loop through each post and extract fields
		for post in data:
			print(f"\nUser ID : {post.get('userId')}")
			print(f"Post ID : {post.get('id')}")
			print(f"Title   : {post.get('title')}")
			print(f"Body    : {post.get('body')}")
	else:
		print("Error: Unexpected response format from the API.")

# Handle timeout errors
except requests.exceptions.Timeout:
	print("Error: The request timed out. Please, try again later.")

# Handle network connection problems
except requests.exceptions.ConnectionError:
	print("Error: Unable to connect to the API. Check your internet connection.")

# Handle HTTP errors like 404 or 500
except requests.exceptions.HTTPError as http_err:
	print(f"HTTP error occurred: {http_err}")

# Handle JSON decoding errors
except ValueError:
	print("Error: Failed to decode the API response.")
