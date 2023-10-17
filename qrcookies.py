import requests
import qrcode
import re


def get_cookies_qr(headers):
    print("准备扫码登录获取cookies")
    url="https://passport.bilibili.com/x/passport-login/web/qrcode/generate"
    response = requests.get(url, headers=headers)
    qrcode_key=response.json()['data']['qrcode_key']
    qr_url=response.json()['data']['url']
    img=qrcode.make(qr_url)
    img.show()
    pass_url="https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key="+qrcode_key
    print("扫码成功登入后请按任意键并回车进行下一步")
    empty=input()
    response = requests.get(pass_url, headers=headers)
    res=response.json()['data']['url']
    match = re.search(r'SESSDATA(.+?)&', res)
    ans=None
    if match:
        ans=match.group()
    return ans
    