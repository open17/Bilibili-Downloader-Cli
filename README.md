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
## 使用
### 运行exe版本
你可以到[releases页面](https://github.com/open17/Bilibili_Downloader_Cli/releases)下载安装二进制版本
### 运行python版本
```shell
git clone https://github.com/open17/Bilibili_Downloader_Cli.git
cd Bilibili_Downloader_Cli
python cli.py
```
## 深入了解
### 文件结构
.
├── cli.py (入口文件,交互命令行)
│  
├── ioer.py (输入输出类) 
│  
├── downloader.py (下载功能类) 
│  
├── qrcookies.py (实现扫码登录并获取cookies) 
│  
└── controller.py (控制ioer,downloader,qrcookies)


