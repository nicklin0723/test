import requests

url = "https://api.trello.com/1/actions/59794c788ee100440fc771a8"

response = requests.request("GET", url)

print(response.text)
