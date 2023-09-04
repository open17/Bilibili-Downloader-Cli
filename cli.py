import getInfo
import cookies
import download
import login
import setting

# options
ops = ['设置cookies(SESSDATA)', '查看headers', '开始下载', '下载设置', '说明','退出']

# default header
headers = {
    'Referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
}

qn_list = ["240P 极速",
           "360P 流畅",
           "480P 清晰",
           "720P 高清",
           "720P60 高帧率",
           "1080P 高清",
           "1080P+ 高码率",
           "1080P60 高帧率",
           "4K 超清"]
qn_map = {
    "240P 极速": "6",
    "360P 流畅": "16",
    "480P 清晰": "32",
    "720P 高清": "64",
    "720P60 高帧率": "74",
    "1080P 高清": "80",
    "1080P+ 高码率": "112",
    "1080P60 高帧率": "116",
    "4K 超清": "120"
}

#默认chunk_size
chunk_size=1024

# 默认清晰度
qn = "80"
qn_word="1080P 高清"

# 设置弹幕(0关)
dm=0

# 设置headers
def setheaders():
    Cookies = cookies.get_cookies()
    if Cookies:
        headers['Cookie'] = Cookies


# 获取headers
def getheaders():
    print("\n当前headers:\n", headers)
    print()

# 清晰度
def check_qn():
    global qn,qn_word
    print("当前清晰度", qn_word,"\n\n")
    for i,qn_w in enumerate(qn_list):
        print(i+1,qn_w)
    print("\n要更改清晰度请输入对应的序号,输入其他任意键退出:",end=" ")
    try:
        idx = int(input())
        qn_word=qn_list[idx-1]
        qn=qn_map[qn_word]
        print("修改完成,当前清晰度:", qn_word)
    except:
        print("返回主界面")


# 更新cookies
def setcookies():
    print("请确认获取cookies方式:\n1 扫码登入自动获取 \n2 手动输入cookies(SESSDATA)值")
    ans = input()
    if ans == "1":
        print("生成登入二维码...")
        SESSDATA = login.qrlogin_return_cookies()
    else:
        print("请输入SESSDATA值: ", end=" ")
        SESSDATA = input()
    cookies.set_cookies(SESSDATA)
    setheaders()
    print("自动更新headers")
    getheaders()

# 多p下载视频
def np_download(bvid, cid_group):
    while 1:
        print("当前视频含有", len(cid_group), "p")
        print("1 单视频下载")
        print("2 批量下载")
        print("3 清晰度")
        print("4 返回")
        print("请输入对应的操作数字: ", end=" ")
        op = input()
        if op == '1':
            print("输入要下载的p号(1 -", len(cid_group), "): ", end=" ")
            id = int(input())-1
            cid = str(cid_group[id]['cid'])
            print("开始下载", cid_group[id]['part'],)
            download.get_mp4(bvid, cid, headers, qn,cid_group[id]['part'],chunk_size,dm)
        if op == '2':
            print("输入要下载的开始p号: ", end=" ")
            s = int(input())-1
            print("输入要下载的结束p号: ", end=" ")
            e = int(input())
            for i in range(s, e):
                cid = str(cid_group[i]['cid'])
                print("开始下载", cid_group[i]['part'])
                download.get_mp4(bvid, cid, headers, qn,cid_group[i]['part'],chunk_size,dm)
        if op == '4':
            print("返回")
            break
        if op == '3':
            check_qn()

# 下载设置
def setting_config():
    global chunk_size,dm
    while 1:
        print("\n\nchunk_size:",chunk_size,"\n清晰度:",qn_word,"\n是否下载弹幕(0否1是):",dm)
        print("\n1 chunk_size设置")
        print("2 清晰度设置")
        print("3 弹幕设置")
        print("4 保存下载设置")
        print("5 返回")
        print("\n请输入对应的操作数字: ", end=" ")
        op = input()
        if op == '1':
            print("当前chunk_size:",chunk_size)
            print("输入y更改chunk_size,输入其他返回")
            ans=input()
            if ans=='y':
                print("请输入新的chunk_size:",end=" ")
                chunk_size=int(input())
                print("当前chunk_size:",chunk_size)
        if op == '2':
            check_qn()
        if op == '3':
            print("当前dm:",dm)
            print("输入y更改dm,输入其他返回")
            ans=input()
            if ans=='y':
                dm^=1
                print("当前dm:",dm)
        if op == '4':
            setting.set_config(qn_word,chunk_size,dm)
            print("当前下载设置已保存")
        if op == '5':
            print("返回")
            break
    
            

# cli主程序
def cli():
    global chunk_size,qn_word,qn,dm
    # 更新headers
    setheaders()
    # 获取配置
    config=setting.get_config()
    if len(config)==3:
        qn_word,chunk_size,dm=config
        chunk_size=int(chunk_size)
        dm=int(dm)
        qn=qn_map[qn_word]
    print("""
              

 ██████╗ ██████╗ ███████╗███╗   ██╗ ██╗███████╗  
 ██╔═══██╗██╔══██╗██╔════╝████╗  ██║███║╚════██║    
 ██║   ██║██████╔╝█████╗  ██╔██╗ ██║╚██║    ██╔╝    
 ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║ ██║   ██╔╝     
 ╚██████╔╝██║     ███████╗██║ ╚████║ ██║   ██║      
  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═╝   ╚═╝      


""")
    while 1:
        print("\n\n")
        for i in range(len(ops)):
            print(i+1, ops[i])
        print()
        print("请输入对应的操作数字: ", end=" ")
        c = input()
        # 退出
        if c == '6':
            break
        # 设置headers
        elif c == '2':
            getheaders()
        # 设置cookies
        elif c == '1':
            setcookies()
        # 下载视频
        elif c == '3':
            print("输入bvid/ep_id:")
            id = input()
            # 如果是bvid
            if id[:2] == "BV":
                bvid = id
                cid_group = getInfo.getcid(bvid, headers)
                # 单p直接下载
                if (len(cid_group) == 1):
                    cid = str(cid_group[0]['cid'])
                    name=cid_group[0]['part']
                    print("开始下载", name)
                    download.get_mp4(bvid, cid, headers, qn, name,chunk_size,dm)
                # 多p下载
                else:
                    np_download(bvid, cid_group)
            # ep_id
            else:
                download.get_mp4_ep_id(id, headers, qn,chunk_size)

        # 下载设置
        elif c == '4':
            setting_config()
        # 说明
        elif c == '5':
            print("""

说明:
                  
1. bvid是什么?
                  
    >bvid即为bv号,b站每个视频现在均有一个对应的bv号,格式为BVxxxx,例如BV19u4y1D7GT
                  
                  
2. 如何获取一个视频的bvid
                  
    >移动端在视频的简介处显示,网页端可查看当前链接获取
    例如视频链接为https://www.bilibili.com/video/BV19u4y1D7GT/?spm_id_from=... , 很明显bvid即为BV19u4y1D7GT
                  
3. cookies(SESSDATA)是什么?有什么用?
                  
    >cookies(SESSDATA)用于某些b站请求的鉴权,比如说如果需要获取一个视频720P及以上其清晰度,便需要设置cookies才能获取(登录)
    你可以采取扫码登录,或者也可以手动输入cookies中SESSDATA对应的值
    你可以查看网上教程得知如何取得b站的cookies

4. epid下载失败?
   > 你可以尝试采取BV号下载的方式,并欢迎来提交issue

5. 下载设置是什么?
   > 目前只可以设置chunk_size这个属性,chunk_size 越大，下载速度越快，但是也越容易导致网络阻塞。
    一般来说，对于网络速度较快的文件，可以将 chunk_size 设置为较大的值，例如 10240 或 102400 字节。
    对于网络速度较慢的文件，可以将 chunk_size 设置为较小的值，例如 1024 或 10240 字节。
                
""")
            
        else:
            print("未知操作")


if __name__ == "__main__":
    cli()
