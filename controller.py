from ioer import ioer
from downloader import downloader
from qrcookies import get_cookies_qr


class controller:
    def __init__(self):
        # 文件控制类
        self.ioer = ioer()
        self.downloader = downloader({})
        self.sync_config()

    def set_none_headers_config(self, qn=None, dm=None, chunk_size=None):
        update_config = {}
        if qn is not None:
            update_config["qn"] = qn
        if dm is not None:
            update_config["dm"] = dm
        if chunk_size is not None:
            update_config["chunk_size"] = chunk_size
        if update_config != {}:
            self.ioer.update_config(update_config)
            self.sync_config()

    # 若当前config不存在时会自动初始化config
    def get_config(self):
        return self.ioer.get_config()

    def reset_config(self):
        self.ioer.reset_config()
        self.sync_config()

    # 当config更新或者初始化时同步更新config给所有类
    def sync_config(self):
        config = self.get_config()
        self.downloader.update_config(config)

    def set_cookies_config(self, cookies):
        if cookies is not None:
            curr_headers = self.get_headers_config()
            curr_headers["cookies"] = cookies
            self.ioer.update_config({"headers":curr_headers})
            self.sync_config()

    def get_headers_config(self):
        return self.get_config()["headers"]
    
    # 当且仅当cookies存在且不等于默认的空白cookies时返回true
    def check_cookies(self):
        if "cookies" in self.get_headers_config().keys():
            cookies=self.get_headers_config()["cookies"]
            if cookies != self.ioer.get_default_config()["headers"]["cookies"]:
                return True
        return False

    def get_cid(self, bvid):
        return self.downloader.get_cid(bvid)

    def download_epid_video(self, epid):
        self.downloader.get_epid_video(epid)

    def download_biv_video_dm(self, bvid, cid, name_raw="Movie"):
        self.downloader.get_bvid_video(bvid, cid, name_raw)
        self.download_dm(cid, name_raw)

    def download_dm(self, cid, name_raw="Movie"):
        self.downloader.download_dm(cid, name_raw)

    def login_update_headers(self):
        headers = self.get_headers_config()
        new_cookies = get_cookies_qr(headers)
        if new_cookies is not None and new_cookies != headers["cookies"]:
            self.set_cookies_config(new_cookies)
