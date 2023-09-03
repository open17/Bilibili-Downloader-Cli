import requests

def get_mp4(bvid,cid,headers,qn="16",name_raw="Movie"):
    url = "https://api.bilibili.com/x/player/playurl?cid="+cid+"&bvid="+bvid+"&qn="+qn
    name=name_raw+'.mp4'
    response=None
    response = requests.get(url, headers=headers)
    video_url = response.json()["data"]["durl"][0]["url"]
    download_mp4(video_url,name,headers)


def download_mp4(url,name,headers):
    print("url请求成功,链接中...\n链接完毕,开始下载MP4,根据视频清晰度与网络流畅度,可能需要一点时间,请耐心等候")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
            print(name,"下载完成")
    else:
        print(name,"下载失败")

def get_mp4_ep_id(ep_id,headers,qn="16"):
    url="https://api.bilibili.com/pgc/player/web/playurl?ep_id="+ep_id[2:]+"&qn="+qn
    name="ep_id_"+ep_id+'.mp4'
    response=None
    response = requests.get(url, headers=headers)
    # print(response.json())
    video_url = response.json()["result"]["durl"][0]["url"]
    download_mp4(video_url,name,headers)