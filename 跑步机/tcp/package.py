# -*- coding: utf-8 -*-
import time
import struct
import hashlib
import AESUtil
from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex



def package(data_aes,cmd,t):
    #####包头#####
    num = len(data_aes)
    Len = struct.pack('>I', 38 + num)
    pro_ver = struct.pack('4s', 'V1.0'.encode('utf-8'))
    app_id = struct.pack('>H', 10010)
    app_ver = bytes([1,0,0])
    #t = (int(time.time()))
    # print('msg_id：', t)
    msg_id = struct.pack('>Q', t)
    # print('msg_id:', msg_id)
    cmd = bytes([cmd])
    key_sign = b'keykeykeykeykey2'
    src = msg_id + data_aes + key_sign
    hash_sha1 = hashlib.sha1()
    hash_sha1.update(src)
    sign_info = hash_sha1.digest()

    # 组包
    result = Len + pro_ver + app_id + app_ver + msg_id + cmd + sign_info + data_aes
    return result



def analysis(recvData):
    #分解
    recvData = b2a_hex(recvData)
    Receive_Data = recvData
    #Receive_Data = recvData.decode('utf-8')

    pro_ver = Receive_Data[0:8]
    app_id = Receive_Data[8:12]
    app_ver = Receive_Data[12:18]
    msg_id_hex = a2b_hex(Receive_Data[18:34])
    msg_id = struct.unpack('>Q', bytes(msg_id_hex))[0]


    cmd = Receive_Data[34:36]
    sign_info = Receive_Data[36:76]
    data_76 = Receive_Data[76:]
    # data解密
    iv = Random.new().read(AES.block_size)
    aes = AESUtil.AESUtil('keykeykeykeykey1', iv)  # 初始化密钥 和 iv
    analysis_aes=aes.decrypt(data_76)[16:]
    #print(analysis_aes)
    return msg_id,analysis_aes
