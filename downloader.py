import requests
import time
import sys


def _get_progress_bar(progress, total):
    """获取可视化图标样式的进度条"""
    width = 40
    filled = int(progress / total * width)
    empty = width - filled
    return "■" * filled + " " * empty


class downloader:
    def __init__(self, config) -> None:
        self.config = config

    def update_config(self, config):
        self.config = config

    def get_bvid_video(self, bvid, cid, name_raw="Movie"):
        url = "https://api.bilibili.com/x/player/playurl?cid="+str(cid)+"&bvid="+bvid+"&qn="+str(self.config["qn"])
        name = name_raw+'.mp4'
        response = None
        response = requests.get(url, headers=self.config["headers"])
        video_url = response.json()["data"]["durl"][0]["url"]
        self.download_video(video_url, name)

    def get_epid_video(self, ep_id):
        url = "https://api.bilibili.com/pgc/player/web/playurl?ep_id=" + \
            ep_id[2:]+"&qn="+self.config["qn"]
        name = "ep_id_"+ep_id+'.mp4'
        response = requests.get(url, headers=self.config["headers"])
        video_url = response.json()["result"]["durl"][0]["url"]
        self.download_video(video_url, name)

    def get_cid(self,bvid):
        url="https://api.bilibili.com/x/player/pagelist?bvid="+bvid
        response = requests.get(url, headers=self.config["headers"])
        return response.json()['data']

    def download_video(self, url, name):
        print("开始下载MP4,根据视频清晰度与网络流畅度,可能需要一点时间,请耐心等候")
        response = requests.get(
            url, headers=self.config["headers"], stream=True)
        name="a.mp4"
        if response.status_code == 200:
            with open(name, 'wb') as file:
                content_length = int(response.headers['Content-Length'])
                progress = 0
                start_time = time.time()
                for chunk in response.iter_content(chunk_size=self.config["chunk_size"]):
                    file.write(chunk)
                    progress += len(chunk)
                    now_time = time.time()
                    estimated_time = (content_length - progress) / \
                        progress * (now_time - start_time)
                    sys.stdout.write("\r[{}] {:.2f}% 用时 {:.0f}s 估计还需要 {:.0f}s".format(
                        _get_progress_bar(progress, content_length),
                        progress / content_length * 100,
                        now_time - start_time,
                        estimated_time))
                    sys.stdout.flush()
                sys.stdout.write("\n下载完成")
        else:
            print(name, "下载失败")

    def download_dm(self, cid, name_raw="Movie"):
        if self.config["dm"]:
            print("开始下载弹幕")
            dm_url = "https://comment.bilibili.com/"+cid+".xml"
            response = requests.get(dm_url, headers=self.config["headers"])
            with open(name_raw+'.xml', 'wb') as file:
                file.write(response.content)
            print("弹幕下载完毕")
    