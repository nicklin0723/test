import requests

url = "https://api.trello.com/1/boards/tBmYPSYe?fields=id,name,idOrganization,dateLastActivity&lists=open&list_fields=id,name"

response = requests.request("GET", url)

print(response.text)
