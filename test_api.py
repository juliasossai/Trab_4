# Requires Python 3.7 or later
import requests

url = "http://localhost:5000/api"

data = {"number": 12, "operations": ["factorial", "fibonacci"]}

response = requests.post(url, json=data)
result = response.json()
if response.status_code != 200:
    print("Error:", result["error"])
    exit(1)


fibonacci_result = result.get("fibonacci")
factorial_result = result.get("factorial")
print("Input:", data["number"])
print("Operations:", data["operations"])
print("Result:", result)
print("Fibonacci:", fibonacci_result)
print("Factorial:", factorial_result)
