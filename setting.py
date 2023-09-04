def set_config(qn_word="1080P 高清",chunk_size=1024,dm=0):
    """
    qn_word 清晰度
    chunk_size 请求大小
    dm 是否下载弹幕
    """
    with open("config.txt", 'w',encoding="utf-8") as file:
        file.write(qn_word+'\n'+str(chunk_size)+'\n'+str(dm)+'\n')

def get_config():
    ans=[]
    try:
        with open("config.txt", "r",encoding="utf-8") as f:
            for line in f:
                ans.append(line[:-1])
    except:
        pass
    return ans


if __name__ == "__main__":
    set_config()
    get_config()
