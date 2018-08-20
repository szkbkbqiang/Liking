# coding:utf-8

import requests
import sign
import time

host = "https://testapi-iot.tslsmart.com"

# 生成sign
ProductKey = "d6c697b2fb0a4eae768821a62b51e906"
# SignData = sign.TSL_sign(body, ProductKey)

def post(body,url):
    SignData = sign.TSL_sign(body, ProductKey)

    data={
        "ProductKey": "d6c697b2fb0a4eae768821a62b51e906",
        "SignData": sign.TSL_sign(body, ProductKey)
    }
    body.update(data)

    print("发送的数据url, body, h：",url, body)
    r1 = requests.post(url, data=body)
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
def device():
    #新增设备接口
    url = host + "/offline/device-report"
    body={
        "StoreId":1 ,
        "DeviceType":6,
        "DeviceId":0,#设备Id
        "Mac":0,
        "DeviceName":0,
        "DeviceModel":0,
        "InstallLocation":0,
        "SoftwareVersion":0,
        "HardwareVersion":0,
        "ICCID":0,
        "NetType":0,
        "FirstOnlineTime":0,

        "Token":0,
          }
    post(body,url)
def village():
    #小区信息更新接口
    url = host + "/village/update"
    body = {
        "village_id": "1",
        "building_id": "1",
        "relation_status": 1
            }
    post(body,url)
def sport():
    #用户运动数据
    url = host + "/user/sport-list"
    body = {
        "last_sync_id": "1"
            }
    post(body,url)
def health():
    #用户健康数据
    url = host + "/user/health-data"
    body = {
        "last_sync_id": "1"
            }
    post(body,url)

# gym()
# village()
# sport()
# health()
device()