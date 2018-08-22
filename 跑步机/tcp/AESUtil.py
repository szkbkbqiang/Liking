#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESUtil:
    def __init__(self, key ,iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size
        # 补位
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, text):

        text = self.pad(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 目前AES-128 足够目前使用

        ciphertext = cryptor.encrypt(text)
        # 把加密后的字符串转化为16进制字符串
        return ciphertext
        # return b2a_hex(ciphertext)

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #plain_text = cryptor.decrypt(text)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text
        # return self.unpad(plain_text.rstrip('\0'))




# if __name__ == '__main__':
#     # iv = "1237635217384736"
#     iv = Random.new().read(AES.block_size)
#     #print('iv:', b2a_hex(iv))
#     pc = AESUtil('keykeykeykeykey1',iv)  # 初始化密钥 和 iv
#     import sys
#
#     #data = data.data()
#     #text = json.dumps(data)
#     import data
#     bracelet = 10000000
#
#     # print(json)
#     while bracelet < 10000001:
#         bracelet += 1
#         d = data.bracelet_id(bracelet)
#         #print(d)
#         src=json.dumps(d)
#
#         #src = '{"cmd":1,"data":{"bracelet_id":"10000001","bracelet_type":1}}'
#
#         #print(type(src))
#
#         #print("原文%d:%s" % (len(src), src))
#         encrypt = pc.encrypt(src)  # 加密
#         print("密文%d:%s" % (len(encrypt), encrypt))
# #         decrypt = pc.decrypt(b2a_hex(b'\xc1\x8f\xb8\xcd\xc5\x00Zmm#\xca\xbc\xa4\xff\x85H\xad\xb1\x0c\xb31a\xec\x9fM\xdc\x08\xca\xad\x9cM\xbbsp?N\xff\x04L\x86\xeb\xed\xf0\xcb\xcd\x9aL\x1f\xab\x1d\xbb\x00E\xfcN\xa7\xbf<\xfd9\x9e\xce))\x8f4\x88\xa6\x1e*E)\xdb\xbauB\xc7\x19)m'
# # ))
#         decrypt = pc.decrypt(b2a_hex(iv+encrypt))
#         print("解密%d:%s" % (len(decrypt), str(decrypt)))

