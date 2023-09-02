import getInfo
import cookies
import download

# options
ops = ['设置/修改cookies(SESSDATA)', '更新headers(变更cookies后需要进行更新)', '开始下载','清晰度','说明','退出']
# default header
headers = {
    'Referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
}

# 默认清晰度
qn="80"

# 设置headers
def setheaders():
    Cookies = cookies.get_cookies()
    if Cookies:
        headers['Cookie'] = Cookies
        print("\nheaders更新成功,当前headers:\n", headers)
        print()

# 清晰度
def check_qn():
    global qn
    print("当前清晰度",qn,"\n输入y修改, n退出:")
    ans=input()
    if ans=='y':
        print("新清晰度:")
        qn=input()


# 更新cookies
def setcookies():
    print("请输入cookies: ", end=" ")
    cookies.set_cookies(input())

# 多p下载视频
def np_download(bvid, cid_group):
    while 1:
        print("当前视频含有", len(cid_group), "p")
        print("1 单视频下载")
        print("2 批量下载")
        print("3 清晰度")
        print("4 退出")
        print("请输入对应的操作数字: ", end=" ")
        op = input()
        if op == '1':
            print("输入要下载的p号(1 -", len(cid_group), "): ", end=" ")
            id = int(input())-1
            cid = str(cid_group[id]['cid'])
            print("开始下载",cid_group[id]['part'],)
            download.get_mp4(bvid, cid, headers,qn)
        if op == '2':
            print("输入要下载的开始p号: ", end=" ")
            s = int(input())-1
            print("输入要下载的结束p号: ", end=" ")
            e = int(input())
            for i in range(s, e):
                cid = str(cid_group[i]['cid'])
                print("开始下载",cid_group[i]['part'],)
                download.get_mp4(bvid, cid, headers,qn)
        if op == '4':
            print("退出")
            break
        if op=='3':
            check_qn()

            


# cli主程序
def cli():
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
        if c == '2':
            setheaders()
        # 设置cookies
        if c == '1':
            setcookies()
        # 下载视频
        if c == '3':
            print("输入bvid/ep_id:")
            id = input()
            # 如果是bvid
            if id[:2]=="BV":
                bvid=id
                cid_group = getInfo.getcid(bvid, headers)
                # 单p直接下载
                if (len(cid_group) == 1):
                    cid = str(cid_group[0]['cid'])
                    print("开始下载",cid_group[0]['part'],)
                    download.get_mp4(bvid, cid, headers,qn)
                # 多p下载
                else:
                    np_download(bvid, cid_group)
            # ep_id
            else:
                download.get_mp4_ep_id(id,headers,qn)

        # 清晰度
        if c=='4':
            check_qn()
        # 说明
        if c=='5':
            print("""

说明:
                  
1. 清晰度数值对应清晰度(默认80)
                  
6 	    240P 极速 	
16 	    360P 流畅 	
32 	    480P 清晰 	
64 	    720P 高清(无720P时则为720P60)
74 	    720P60 高帧率 	
80 	    1080P 高清 	
112     1080P+ 高码率 	
116     1080P60 高帧率 	
120     4K 超清 	

                  
2. bvid是什么?
                  
bvid即为bv号,b站每个视频现在均有一个对应的bv号,格式为BVxxxx,例如BV19u4y1D7GT
                  
                  
3. 如何获取一个视频的bvid
                  
移动端在视频的简介处显示,网页端可查看当前链接获取
例如视频链接为https://www.bilibili.com/video/BV19u4y1D7GT/?spm_id_from=...,很明显bvid即为BV19u4y1D7GT
                  
4. cookies(SESSDATA)是什么?有什么用?
                  
cookies(SESSDATA)用于伪装b站登入,也就是说如果需要获取720P及以上其清晰度,通常需要设置cookies才能获取
你可以查看网上教程得知如何取得b站的cookies,然后你只需要输入cookies中SESSDATA对应的值即可
                  
5. 设置了cookies还是不能下载1080p(或其他)视频?
                  
首先,检查是否更新headers;其次,查看cookies是否设置正确以及查看清晰度数是否正确;此外确保该视频本身存在1080p(或其他)清晰度的版本.
如果还是不行,请通过https://api.bilibili.com/x/player/playurl? 手动构造get请求检查返回视频清晰度,欢迎来提issues
                  
""")


if __name__ == "__main__":
    cli()
