import requests


def get_titles():
    titles=[]
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php").json()
    for i in response['posts']:
        titles.append(i["title"])

    return titles


print(get_titles())
