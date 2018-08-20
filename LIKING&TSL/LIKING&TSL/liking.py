# coding:utf-8






import requests
import sign
import time
host = "https://devapi.likingfit.com"

def post(body,url):

    #生成sign

    timestamp=str(int(time.time()))
    h = {
        "appid": "853727357",
        "request-id": "1234567890",
        # "timestamp": '1532488198',
        "timestamp": timestamp,
        "api-version": "1.0",
        "sign":sign.LK_sign(timestamp,body)
        }

    #s = requests.session()   #不要写死session
    print("发送的数据url, body, h：",url, body, h)
    r1 = requests.post(url, data=body, headers=h)
    r1 = r1.text
    print("接收返回的值：",r1)

    #r1.encode(encoding='utf-8').decode()
    # decodestr = base64.b64decode(r1.encode("utf-8"))
    # print(decodestr)
    # iv ='8Rt9Cxg3e4VjQqak'
    # aes = AESUtil.AESUtil('5vu4cYhDizqcgRjX', iv)  # 初始化密钥 和 iv
    # analysis_aes = aes.decrypt(decodestr)
    # print("analysis_aes：",analysis_aes)

    # return r1.content  # python2的return这个
    return r1  # python3
def gym():
    #健身房信息接口
    url = host + "/gym/list"
    body={"last_sync_id":""}
    post(body,url)
def village():
    #小区信息更新接口
    url = host + "/village/update"
    body = {
        "village_id": "435ec7d4ce8a6481d2f671ca277ce4bd",
        "building_id": "0019f08066a560e2e6bb6ba401b9e39d",
        "relation_status":"1"
            }
    post(body,url)
def sport():
    #用户运动数据
    url = host + "/user/sport-list"
    body = {
        "last_sync_id": ""
            }
    post(body,url)
def health():
    #用户健康数据
    url = host + "/user/health-data"
    body = {
        "last_sync_id": ""
            }
    post(body,url)

gym()
village()
sport()
health()