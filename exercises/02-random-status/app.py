import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

if response.status_code == 404:
    print(f'The URL you asked is not found\n')  
elif response.status_code == 503:
    print (f'Unavailable right now\n')
elif response.status_code == 200:
    print (f'Everything went perfect\n')
elif response.status_code == 400:
    print(f'Something is wrong on the request params\n')
else:
    print(f'Status code: {response.status_code}')

