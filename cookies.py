def set_cookies(cookies:str):
    with open('cookies.txt', 'w') as file:
        file.write("SESSDATA="+cookies)
    print("cookies设置完成")

def get_cookies():
    try:
        file = open('cookies.txt', 'r') 
        content = file.read()
        file.close()
        return content
    except:
        # print("未发现cookies配置,请先设置cookies")
        pass

if __name__ == "__main__":
    set_cookies("")
    print(get_cookies())