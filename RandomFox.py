from urllib import response
import requests
import webbrowser

# Create variable to store all data from API call
response = requests.get("https://randomfox.ca/floof")

# Prints the status code of connection. 200 designates a successful connection.
print(response.status_code)

# Returns the value as a string
print(response.text)

# Returns a dictionary object that we can work with
print(response.json())

# Store the return dictionary in a variable and print the 'value' from 'key'
fox = response.json()
print(fox['image'])

webbrowser.open(fox['image'])