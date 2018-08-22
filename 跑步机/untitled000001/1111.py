# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os
import json
#在进行加密/解密前，只需使用 pad/unpad 进行填充/截断即可
data = [{
        'device_id': 'a000000100010001',  # 设备ID string
    'gateway_id': '',  # 网关设备ID string
    'device_name':'力量区人感', # 设备名称 string
    'device_type': 26, # 无硬件迭代不扩展 int8
    'control_num': '3',  # 设备控制点数，如开关下辖三路灯。 Int32
    'online_status': '0',  # 设备在线状态，0离线 1在线 int8
    'battery_status': 1,  # 设备电量状态，0不足 1充足，无电量属性设备默认为1 int8
    'device_status': 0,# 设备运行状态，0关，1开，2暂停 int8
    'bluetooth_mac':'AABBCCDDEEFFGG',  # 蓝牙mac地址
    'ethernet_mac':'GGFFEEDDCCBBAA'  # 以太网mac地址
    }
    ]




BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

key = os.urandom(16) # the length can be 长度可以是(16, 24, 32)
json = json.dumps(data)
    #print(json)

    # 获取用户输入十进制数
text = json

cipher = AES.new('keykeykeykeykey1')
encrypted = cipher.encrypt(pad(text)) #.encode('hex')
#encrypted = cipher.encrypt(pad(text))
print(encrypted)  # will be something like 输出什么样的数据'f456a6b0e54e35f2711a9fa078a76d16'

decrypted = unpad(cipher.decrypt())
# decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
print(decrypted)  # will be 'to be encrypted'将被加密

