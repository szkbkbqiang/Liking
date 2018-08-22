# -*- coding: cp936 -*-
#A Test to Return a AES-File of a Common File

from Crypto.Cipher import AES
from Crypto import Random
import binascii

def AES_File(fs):
    key = b'1234567890!@#$%^' #16-bytes password
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print('if fs is a multiple of 16...')
    #if fs is a multiple of 16
    x = len(fs) % 16
    print('fs的长度是： ', len(fs))
    print('The num to padded is : ', x)
    if x != 0:
        fs_pad = fs + '0'*(16 - x) #It shoud be 16-x not
        print('fs_pad is : ', fs_pad)
        print(len(fs_pad))
        print(len(fs_pad)%16)
    msg = iv + cipher.encrypt(fs_pad)
    print('File after AES is like...', binascii.b2a_hex(msg[:10]))
    return msg

#Create a Test Src File and Get FileSteam
fs = open('test', 'w+')
fs.write('啊，我爱你，我的祖国！')
fs.write('凌晨三时开始进攻！')
fs.seek(0,0)
fs_msg = fs.read()
print(fs_msg)
fs.close()

#Crypt Src FileStream
fc = open('fc', 'wb')
fc_msg = AES_File(fs_msg)
fc.writelines(fc_msg)
fc.close()

#raw_input('Enter for Exit...')

# 1. 第一行的‘-*-coding:cp936 -*-’用于告诉Python解释器源码文件的编码方式，Python的默认方式是ASCii的，但是由于代码中出现了汉字，因此运行时解释器会提示我们是否要注明解码的方式，也可以使用'coding:utf-8'；
# -2. 第四行到第六行主要引入一些必要的模块，Crypto.Cipher模块中的AES模块以及Crypto中的Random模块，binascii模块为查看二进制下的数据提供了各种方法。
# -3. 第八行到二十四行主要实现调用AES加密API的函数，我们命名为AES_File()，其中：
#    第九行用于指定AES加密的初始密钥，根据AES规范，可以是16字节、24字节和32字节长，这里我们使用了一个16字节的初始密钥，其实完全可以由用户输入的口令+salt获得；
#    第十行是用于生成iv，这里使用了Crypto模块中的Random模块，读取其16字节的数据作为iv的值，AES的分块大小固定为16字节；
#    第十一行用于生成了加密时需要的实际密码，主要使用了AES.new(key, AES.MODE_CBC,iv)函数，key和iv由前两步生成，这步可以指定加密模式，这里选择的是CBC模式；
#    第十二到第二十一行主要用于判断数据长度是否为16字节块的整数倍，从而进行适当的Padding，这里的关键是利用'%'运算判断是否是16字节的整数倍，然后在尾部追加(16-x)个填充字符；
#    其实这里还有一个关键的问题，那就是Python中列表和字符串的转换问题。使用list()函数可以将字符串转换成列表，使用str()函数可以将列表转换成字符串，但是前后的转换并不是等价的，比如：
#    可以看到a与c并不相等，将字符串转换成列表时，二者还是元素个数相等的，但是将列表转换成字符串时，会包含进“无关字符”，即'[]'、' '（空格）等，因此元素个数会发生改变。因此列表和字符串是不等价的转换。之所以想到了这个问题，是因为自己在考虑填充时开始想利用列表的append()方法写个循环，结果行不通，最后还是利用了序列乘法予以了解决。
# -4. 第二十二行使用生成的cipher对象的encrypt方法加密文件流，得到密文文件流msg，注意这里与iv进行了一次异或，另一个需要注意的是encrypt方法的输入和输出都是一个字符串；
# -5. 第二十三行主要是为了调试的需要，导入binascii模块查看密文文件流的前10个字节，每个二进制字节以十六进制的形式表示；
# -6. 第二十七行到第三十三行的工作是生成一个明文文件，获取其明文数据流，这里可以直接从打开的文件中读取，不过为了测试的需要，这里临时写入一个文件，因此复制数据流的时候记得重置指针到文件开头，即fs.seek(0, 0)；
# -7. 第三十五行到第三十九行主要是将获取的明文数据流调用AES加密得到密文数据流，然后关闭文件；
#    好了，现在我们看看结果，这里指定编码的时候不影响程序执行，但是会影响程序的print结果，第一次使用utf-8编码，第二次使用ascii编码：