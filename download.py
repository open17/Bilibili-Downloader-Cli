import requests
import time
import sys


def get_mp4(bvid, cid, headers, qn="16", name_raw="Movie", chunk_size=-1,dm=0):
    url = "https://api.bilibili.com/x/player/playurl?cid="+cid+"&bvid="+bvid+"&qn="+qn
    name = name_raw+'.mp4'
    response = None
    response = requests.get(url, headers=headers)
    video_url = response.json()["data"]["durl"][0]["url"]
    download_mp4(video_url, name, headers, chunk_size)
    if dm==1:
        print("开始下载弹幕")
        dm_url="https://comment.bilibili.com/"+cid+".xml"
        response = requests.get(dm_url, headers=headers)
        with open(name_raw+'.xml', 'wb') as file:
            file.write(response.content)
        print("弹幕下载完毕")



def download_mp4(url, name, headers, chunk_size):
    print("url请求成功,链接中...\n链接完毕,开始下载MP4,根据视频清晰度与网络流畅度,可能需要一点时间,请耐心等候")
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(name, 'wb') as file:
            content_length = int(response.headers['Content-Length'])
            progress = 0
            start_time = time.time()
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
                progress += len(chunk)
                now_time = time.time()
                estimated_time = (content_length - progress) / progress * (now_time - start_time)
                sys.stdout.write("\r[{}] {:.2f}% 用时 {:.0f}s 估计还需要 {:.0f}s".format(
                    _get_progress_bar(progress, content_length),
                    progress / content_length * 100,
                    now_time - start_time,
                    estimated_time))
                sys.stdout.flush()
            sys.stdout.write("\n下载完成")
    else:
        print(name, "下载失败")


def _get_progress_bar(progress, total):
    """获取可视化图标样式的进度条"""
    width = 40
    filled = int(progress / total * width)
    empty = width - filled
    return "■" * filled + " " * empty


def get_mp4_ep_id(ep_id, headers, qn="16", chunk_size=-1):
    url = "https://api.bilibili.com/pgc/player/web/playurl?ep_id=" + \
        ep_id[2:]+"&qn="+qn
    name = "ep_id_"+ep_id+'.mp4'
    response = None
    response = requests.get(url, headers=headers)
    video_url = response.json()["result"]["durl"][0]["url"]
    download_mp4(video_url, name, headers, chunk_size)
