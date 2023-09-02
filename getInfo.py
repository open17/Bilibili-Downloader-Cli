import requests
def getcid(bvid,headers):
    url="https://api.bilibili.com/x/player/pagelist?bvid="+bvid
    response = requests.get(url, headers=headers)
    return response.json()['data']