import hashlib
import time
import operator


def LK_sign(timestamp,body):
    h = {
        "appid": "853727357",
        "request-id": "1234567890",
        "timestamp": timestamp,
        # "timestamp": str(int(time.time())),
        "api-version": "1.0"

    }
    h.update(body)
    sorted_h=sorted(h.items(),key = operator.itemgetter(0))#按照item中的第一个字符进行排序，即按照key排序
    #sorted_x=sorted(x.items(),key=operator.itemgetter(1))#这里改为按照item的第二个字符排序，即value排序
    signA=""
    for key in dict(sorted_h):
        signA +=  str(dict(sorted_h)[key])
    #print(signA)
    appScrect = 'UHt5xYytddk7FXsu1fQ9q'
    stringSignTemp = signA + appScrect
    #print(stringSignTemp)
    sign=hashlib.sha1(stringSignTemp.encode('utf-8')).hexdigest()
    # sign=hashlib.sha1(stringSignTemp.encode('utf-8')).hexdigest()
    #print(sign)
    # hash_sha1 = hashlib.sha1()
    # hash_sha1.update(stringSignTemp.encode('utf-8'))
    # sign = hash_sha1.hexdigest()
    # print(sign)
    return sign


def TSL_sign(body,ProductKey):
    h = {
        "ProductKey": 'd6c697b2fb0a4eae768821a62b51e906'
    }

    h.update(body)
    sorted_h = sorted(h.items(), key=operator.itemgetter(0))  # 按照item中的第一个字符进行排序，即按照key排序
    # sorted_h=sorted(h.items(),key=operator.itemgetter(1))#这里改为按照item的第二个字符排序，即value排序
    # print(sorted_h)
    signA = ''
    for key in dict(sorted_h):
        # print(key+"="+str(dict(sorted_h)[key]))
        signA += key + "=" + str(dict(sorted_h)[key]) + "&"
    payload = signA[0:(len(signA) - 1)]
    # print(payload)
    payload = payload + ProductKey
    payload = payload.lower()
    md_payload = hashlib.md5(payload.encode('utf-8')).hexdigest()

    # print(md_payload)

    return md_payload

# if __name__ == "__main__":
#     a=sign()
#     print(a)

