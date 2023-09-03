# Bilibili Downloader Cli
一个简易轻便的b站下载器,支持下载视频,番剧,电影
## 功能
- [x] 下载普通视频 
- [x] 下载多P视频
- [x] 下载番剧
- [x] 下载电影(需要额外付费电影除外)
- [ ] 下载音乐
- [x] 切换画质
- [x] 扫码登录/手动输入cookies
- [x] 支持BV号/EP号下载 

## 使用
### 运行exe版本
你可以到[releases页面](https://github.com/open17/Bilibili_Downloader_Cli/releases)下载安装二进制版本
### 运行python版本
```shell
git clone https://github.com/open17/Bilibili_Downloader_Cli.git
cd Bilibili_Downloader_Cli
python cli.py
```


## 其它说明                  
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
   > 目前只可以设置chunk_size这个属性,chunk_size 越大，下载速度越快，但是也越容易导致网络阻塞。一般来说，对于网络速度较快的文件，可以将 chunk_size 设置为较大的值，例如 10240 或 102400 字节。对于网络速度较慢的文件，可以将 chunk_size 设置为较小的值，例如 1024 或 10240 字节。