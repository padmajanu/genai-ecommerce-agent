import requests

response = requests.post("http://127.0.0.1:8000/ask", json={"question": "What is the total ad sales?"})
print(response.json())
