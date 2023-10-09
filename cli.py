from controller import controller


def cli():
    # 初始化
    co = init()
    show_config(co)
    # options
    ops = ['设置', '下载', '退出']

    while True:
        check_cookies(co)
        for i in range(len(ops)):
            print(i+1, ops[i])
        print("请输入对应的操作数字: ", end=" ")
        opt = input()
        if opt == '1':
            config_cli(co)
        elif opt == '2':
            download_cli(co)
        elif opt == '3':
            break
        else:
            print("输入错误,请重新输入")


def download_cli(co: controller):
    print("输入bvid/ep_id:")
    id = input()
    # 如果是bvid
    if id[:2] == "BV":
        bvid = id
        cid_group = co.get_cid(bvid)
      # 单p直接下载
        if (len(cid_group) == 1):
            p_download(co, bvid, cid_group)
      # 多p下载
        else:
            np_download(co, bvid, cid_group)
    # ep_id
    else:
        spid = id
        co.download_epid_video(spid)


def p_download(co, bvid, cid_group):
    cid = str(cid_group[0]['cid'])
    name = cid_group[0]['part']
    print("开始下载", name)
    co.download_biv_video_dm(bvid, cid, name)


def np_download(co, bvid, cid_group):
    while 1:
        print("当前视频含有", len(cid_group), "p")
        print("1 单视频下载")
        print("2 批量下载")
        print("3 返回")
        print("请输入对应的操作数字: ", end=" ")
        op = input()
        if op == '1':
            print("输入要下载的p号(1 -", len(cid_group), "): ", end=" ")
            id = int(input())-1
            cid = str(cid_group[id]['cid'])
            name = cid_group[id]['part']
            print("开始下载", name,)
            co.download_biv_video_dm(bvid, cid, name)
        if op == '2':
            print("输入要下载的开始p号: ", end=" ")
            s = int(input())-1
            print("输入要下载的结束p号: ", end=" ")
            e = int(input())
            for i in range(s, e):
                cid = str(cid_group[i]['cid'])
                name = cid_group[i]['part']
                print("开始下载", name)
                co.download_biv_video_dm(bvid, cid, name)
        if op == '3':
            print("返回")
            break
        else:
            print("输入错误，请重新输入")


def config_cli(co: controller):
    while 1:
        print("\n\n这里是设置界面")
        ops = ["查看配置", "登录(headers)", "弹幕设置(dm)", "清晰度设置(qn)",
               "下载切片大小设置(chunk_size)", "说明", "同步配置", "重置设置", "返回"]
        for i in range(len(ops)):
            print(i+1, ops[i])
        print("请输入对应的操作数字: ", end=" ")
        opt = input()
        if opt == '1':
            show_config(co)
        elif opt == '2':
            co.login_update_headers()
        elif opt == '3':
            dm_cli(co)
        elif opt == '4':
            qn_cli(co)
        elif opt == '5':
            chunk_size_cli(co)
        elif opt == '6':
            usebook()
        elif opt == '7':
            co.sync_config()
        elif opt == '8':
            co.reset_config()
        elif opt == '9':
            break
        else:
            print("输入错误,请重新输入")


def usebook():
    print("1. 你可以直接修改config.json文件来更新任何的设置,也可以通过cli交互更改")
    print("2. 如果你不知道怎么修改config.json文件,请直接通过cli交互更改")
    print("3. 手动修改config.json后请在设置中运行同步配置")
    print("4. chunk_size 越大，下载速度越快，但是也越容易导致网络阻塞。一般来说，网络速度较快时可以将 chunk_size 设置为较大的值，例如 10240 或 102400 字节。网络速度较慢,为了避免堵塞，可以将 chunk_size 设置为较小的值，例如 1024 或 10240 字节。dm决定是否下载弹幕,True下载,False不下载,初始默认值为True.qn为清晰度.")


def chunk_size_cli(co: controller):
    print("请输入下载切片大小: ", end=" ")
    chunk_size = int(input())
    co.set_none_headers_config(chunk_size=chunk_size)
    print("切片大小设置成功")


def qn_cli(co: controller):
    print("请输入清晰度: \n")
    qn_list = ["240P 极速",
               "360P 流畅",
               "480P 清晰",
               "720P 高清",
               "720P60 高帧率",
               "1080P 高清",
               "1080P+ 高码率",
               "1080P60 高帧率",
               "4K 超清"]
    qn_list_num = [6, 16, 32, 64, 74, 80, 112, 116, 120]
    for i in range(len(qn_list)):
        print(i+1, qn_list[i])
    print("请输入对应的操作数字: ", end=" ")
    opt = input()
    if int(opt) > len(qn_list_num):
        print("输入错误,请重新输入")
    else:
        co.set_none_headers_config(qn=qn_list_num[int(opt)-1])


def dm_cli(co: controller):
    print("是否下载弹幕?")
    print("1.下载弹幕")
    print("2.不下载弹幕")
    print("3.退出")
    print("请输入对应的操作数字: ", end=" ")
    opt = input()
    if opt == '1':
        ans = True
    elif opt == '2':
        ans = False
    else:
        return
    co.set_none_headers_config(dm=ans)


def check_cookies(co: controller):
    if co.check_cookies():
        print("已登录")
    else:
        print("当前状态:未登录b站账号")
        print("未登录状态会影响一些下载功能,比如大会员番剧下载,视频1080p下载等,如有这方面需求,请在设置界面完成登录")


def show_config(co):
    print("\n当前配置:")
    config = co.get_config()
    for i in config.keys():
        if type(config[i]) != dict:
            print(i, ":", config[i])
        else:
            for j in config[i].keys():
                print(i, ":", j, ":", config[i][j])


def init():
    co = controller()
    print("初始化完成")
    return co


if __name__ == "__main__":
    cli()
