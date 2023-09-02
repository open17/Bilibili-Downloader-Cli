import requests

def get_mp4(bvid,cid,headers,qn="16"):
    url = "https://api.bilibili.com/x/player/playurl?cid="+cid+"&bvid="+bvid+"&qn="+qn
    # print(url)
    response=None
    response = requests.get(url, headers=headers)
    video_url = response.json()["data"]["durl"][0]["url"]
    print("url请求成功,链接中...\n链接完毕,开始下载MP4,根据视频清晰度与网络流畅度,可能需要一点时间,请耐心等候")
    # print(video_url)
    response = requests.get(video_url, headers=headers)
    name=bvid+'_'+cid+'.mp4'
    if response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(response.content)
            print(name,"下载完成")
    else:
        print(name,"下载失败")
