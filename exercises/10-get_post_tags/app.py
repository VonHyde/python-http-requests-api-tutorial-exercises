import requests

def get_post_tags(post_id):
    postdict= []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php").json()

    for i in response['posts']:
        if i['id'] == post_id:
            postdict.append(i['tags'])

    return postdict


print(get_post_tags(146))