import requests
import json
import time
def prettify(data):
    print(json.dumps(data, indent=4))

def get_all_tags():
    url = "https://solved.ac/api/v3/tag/list"
    res = requests.get(url)
    return res.json()['items']

def get_tag_info(taglist):
    ret = []
    for cur in taglist:
        ret.append({'id': cur['key'], 'tier': get_avg_tier(cur['key'])})
        print(ret[-1])
        time.sleep(1)
    return ret

def get_avg_tier(tag):
    url = "https://solved.ac/api/v3/search/problem"
    params = {
        'query': f'#{tag}',
        'sort': 'solved',
        'direction': 'desc',
        'page': 1,
    }
    res = requests.get(url, params=params)

    sum_tier = 0
    sum_solved = 0
    for i in res.json()['items']:
        sum_tier += i['level'] * i['acceptedUserCount']
        sum_solved += i['acceptedUserCount']

    return sum_tier // sum_solved 

A = get_all_tags()
B = get_tag_info(A)
prettify(B)
# get_avg_tier("hld")

with open('output.json', 'w') as outfile:
    json.dump(B, outfile, indent=4)