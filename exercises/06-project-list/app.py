import requests

# your code here

response = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php').json()

print(f"Respuesta: {response[1]['name']}")