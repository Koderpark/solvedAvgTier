import requests
import json

def prettify(data):
    print(json.dumps(data, indent=4))

def get_all_tags():
    url = "https://solved.ac/api/v3/tag/list"
    res = requests.get(url)
    return res.json()['items']

def get_tag_info(taglist):
    ret = []
    for cur in taglist:
        ret.append({'id': cur['key']})
    return ret

A = get_all_tags()
B = get_tag_info(A)
prettify(B)