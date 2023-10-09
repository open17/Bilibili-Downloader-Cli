import json
import os


class ioer:
    def __init__(self, path="config.json") -> None:
        self.path = path
        self.default_config = {
            "dm": False,
            "qn": 80,
            "chunk_size": 1024,
            "headers": {
                'Referer': 'https://www.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
                "cookies": "SESSDATA=;"
            }
        }

    def get_default_config(self):
        return self.default_config

    def reset_config(self):
        self.write(self.default_config)

    # cofig参数传入需要更新的config内容
    def update_config(self, update_config={}):
        curr_config = self.get_config()
        for i in update_config.keys():
            curr_config[i] = update_config[i]
        self.write(curr_config)

    def get_config(self):
        if not os.path.exists(self.path):
            self.reset_config()
        return self.read()

    def read(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def write(self, config):
        with open(self.path, "w") as f:
            json.dump(config, f)
