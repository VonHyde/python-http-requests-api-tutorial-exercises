import requests

# your code here

response = requests.get('https://assets.breatheco.de/apis/fake/sample/project1.php').json()

print(response['name'])