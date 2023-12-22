import requests

def get_attachment_by_id(attachment_id):
    postdict= []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php").json()

    for i in response['posts']:
        for x in i['attachments']:
            if x["id"] == attachment_id:
                postdict.append(i['attachments'])

    return postdict

print(get_attachment_by_id(137))