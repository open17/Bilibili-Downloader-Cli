<div align="center">
    <h1 href=" open17.github.io/vuepress-theme-qbook/" align="center">Bilibili Downloader Cli</h1>
    <p align="center">< 轻量级b站视频下载器 ></p>
    <p align="center">
        <a href=""><img src="https://img.shields.io/badge/下载-视频-pink?style=flat-square" alt="video"></a>
         <a href=""><img src="https://img.shields.io/badge/下载-番剧-red?style=flat-square" alt="fan"></a>
         <a href=""><img src="https://img.shields.io/badge/下载-弹幕-green?style=flat-square" alt="dm"></a>
         <a href=""><img src="https://img.shields.io/badge/下载-电影电视剧-blue?style=flat-square" alt="movie"></a>
        <a href="https://github.com/open17/Bilibili_Downloader_Cli/issues/new/choose" target="_blank">
            <img src="https://img.shields.io/static/v1?label=feedback&message=issues&color=orange&style=flat-square">
        </a>
    </p>

</div>

****
## 功能
- [x] 下载普通视频 
- [x] 下载多P视频
- [x] 下载番剧
- [ ] <del>下载音频</del>
- [x] 下载电影(需要额外付费电影除外)
- [x] 下载电视剧 
- [x] 下载xml实时弹幕
- [x] 切换画质
- [x] 扫码登录/手动输入cookies
- [x] 支持BV号/EP号下载 
> 注: 鉴于b站音频区在app新版已经不可见,音频下载不再作为目标功能,但你依然可以通过分离下载视频的音频部分实现音频下载
## 更新
- 2023.10.09 重构全部代码,优化交互逻辑
## 安装&使用
### 二进制版本
你可以到[releases页面](https://github.com/open17/Bilibili_Downloader_Cli/releases)下载安装二进制版本
### python版本
```shell
git clone https://github.com/open17/Bilibili_Downloader_Cli.git
cd Bilibili_Downloader_Cli
pip install -r requirements.txt
python cli.py
```
## 其他说明
1. 你可以直接修改config.json文件来更新任何的设置,也可以通过cli交互更改
2. 如果你不知道怎么修改config.json文件,请直接通过cli交互更改
3. 手动修改config.json后请在设置中运行同步配置
4. chunk_size 越大，下载速度越快，但是也越容易导致网络阻塞。一般来说，网络速度较快时可以将 chunk_size 设置为较大的值，例如 10240 或 102400 字节。网络速度较慢,为了避免堵塞，可以将 chunk_size 设置为较小的值，例如 1024 或 10240 字节。dm决定是否下载弹幕,True下载,False不下载,初始默认值为True.qn为清晰度.
## 深入了解
### 文件结构
```
.
├── cli.py (入口文件,交互命令行)
│  
├── ioer.py (输入输出类) 
│  
├── downloader.py (下载功能类) 
│  
├── qrcookies.py (实现扫码登录并获取cookies) 
│  
├── tester.py (测试) 
│  
└── controller.py (控制ioer,downloader,qrcookies)
```



