import requests

print("Connecting to the internet using Python...")
response = requests.get("https://github.com")
print(f"GitHub API Status Code: {response.status_code}")
print("Task 4 Python app executed successfully!")
