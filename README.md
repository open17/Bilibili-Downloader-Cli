# Bilibili Downloader Cli
一个简易的b站视频下载器
## 特征
- [x] 下载普通视频
- [x] 下载多P视频
- [ ] 下载番剧
- [x] 切换画质

## 使用
```shell
python cli.py
```
或者到releases页面下载安装

## 其它说明
1. 清晰度数值对应清晰度(默认80)
    |清晰度数值|清晰度|
    |---   |---           |
    |6 	|    240P 极速| 	
    |16 |	    360P 流畅| 	
    |32 |	    480P 清晰 |	
    |64 |	    720P 高清(无720P时则为720P60)|
    |74 |	    720P60 高帧率 |	
    |80 |	    1080P 高清 	|
    |112|     1080P+ 高码率| 	
    |116|     1080P60 高帧率| 	
    |120|     4K 超清 	|

                  
2. bvid是什么?
                  
    >bvid即为bv号,b站每个视频现在均有一个对应的bv号,格式为BVxxxx,例如BV19u4y1D7GT
                  
                  
3. 如何获取一个视频的bvid
                  
    >移动端在视频的简介处显示,网页端可查看当前链接获取
    例如视频链接为https://www.bilibili.com/video/BV19u4y1D7GT/?spm_id_from=... , 很明显bvid即为BV19u4y1D7GT
                  
4. cookies(SESSDATA)是什么?有什么用?
                  
    >cookies(SESSDATA)用于伪装b站登入,也就是说如果需要获取720P及以上其清晰度,通常需要设置cookies才能获取
    你可以查看网上教程得知如何取得b站的cookies,然后你只需要输入cookies中SESSDATA对应的值即可
                  
5. 设置了cookies还是不能下载1080p(或其他)视频?
                    
    >首先,检查是否更新headers;其次,查看cookies是否设置正确以及查看清晰度数是否正确;此外确保该视频本身存在1080p(或其他)清晰度的版本.
    如果还是不行,请通过https://api.bilibili.com/x/player/playurl? 手动构造get请求检查返回视频清晰度,欢迎来提issues