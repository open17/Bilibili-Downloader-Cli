import requests
import qrcode
import re

def qrlogin_return_cookies():
    headers = {
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    }
    url="https://passport.bilibili.com/x/passport-login/web/qrcode/generate"
    response = requests.get(url, headers=headers)
    print(response.json())
    qrcode_key=response.json()['data']['qrcode_key']
    qr_url=response.json()['data']['url']
    img=qrcode.make(qr_url)
    img.show()
    pass_url="https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key="+qrcode_key
    print("扫码成功登入后请按任意键并回车继续")
    empty=input()
    response = requests.get(pass_url, headers=headers)
    res=response.json()['data']['url']
    match = re.search(r'SESSDATA(.+?)&', res)
    if match:
      return match.group()[9:-1]