import requests

url = "https://trello.com/b/xV63Lw5W/welcome-board"

response = requests.request("GET", url)

print(response.text)
