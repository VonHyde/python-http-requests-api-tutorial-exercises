import requests

# your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php").json()

print(response["posts"][0]['author']['name'])