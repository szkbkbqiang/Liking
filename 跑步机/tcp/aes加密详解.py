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
    print('fs�ĳ����ǣ� ', len(fs))
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
fs.write('�����Ұ��㣬�ҵ������')
fs.write('�賿��ʱ��ʼ������')
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

# 1. ��һ�еġ�-*-coding:cp936 -*-�����ڸ���Python������Դ���ļ��ı��뷽ʽ��Python��Ĭ�Ϸ�ʽ��ASCii�ģ��������ڴ����г����˺��֣��������ʱ����������ʾ�����Ƿ�Ҫע������ķ�ʽ��Ҳ����ʹ��'coding:utf-8'��
# -2. �����е���������Ҫ����һЩ��Ҫ��ģ�飬Crypto.Cipherģ���е�AESģ���Լ�Crypto�е�Randomģ�飬binasciiģ��Ϊ�鿴�������µ������ṩ�˸��ַ�����
# -3. �ڰ��е���ʮ������Ҫʵ�ֵ���AES����API�ĺ�������������ΪAES_File()�����У�
#    �ھ�������ָ��AES���ܵĳ�ʼ��Կ������AES�淶��������16�ֽڡ�24�ֽں�32�ֽڳ�����������ʹ����һ��16�ֽڵĳ�ʼ��Կ����ʵ��ȫ�������û�����Ŀ���+salt��ã�
#    ��ʮ������������iv������ʹ����Cryptoģ���е�Randomģ�飬��ȡ��16�ֽڵ�������Ϊiv��ֵ��AES�ķֿ��С�̶�Ϊ16�ֽڣ�
#    ��ʮһ�����������˼���ʱ��Ҫ��ʵ�����룬��Ҫʹ����AES.new(key, AES.MODE_CBC,iv)������key��iv��ǰ�������ɣ��ⲽ����ָ������ģʽ������ѡ�����CBCģʽ��
#    ��ʮ�����ڶ�ʮһ����Ҫ�����ж����ݳ����Ƿ�Ϊ16�ֽڿ�����������Ӷ������ʵ���Padding������Ĺؼ�������'%'�����ж��Ƿ���16�ֽڵ���������Ȼ����β��׷��(16-x)������ַ���
#    ��ʵ���ﻹ��һ���ؼ������⣬�Ǿ���Python���б���ַ�����ת�����⡣ʹ��list()�������Խ��ַ���ת�����б�ʹ��str()�������Խ��б�ת�����ַ���������ǰ���ת�������ǵȼ۵ģ����磺
#    ���Կ���a��c������ȣ����ַ���ת�����б�ʱ�����߻���Ԫ�ظ�����ȵģ����ǽ��б�ת�����ַ���ʱ������������޹��ַ�������'[]'��' '���ո񣩵ȣ����Ԫ�ظ����ᷢ���ı䡣����б���ַ����ǲ��ȼ۵�ת����֮�����뵽��������⣬����Ϊ�Լ��ڿ������ʱ��ʼ�������б��append()����д��ѭ��������в�ͨ����������������г˷������˽����
# -4. �ڶ�ʮ����ʹ�����ɵ�cipher�����encrypt���������ļ������õ������ļ���msg��ע��������iv������һ�������һ����Ҫע�����encrypt������������������һ���ַ�����
# -5. �ڶ�ʮ������Ҫ��Ϊ�˵��Ե���Ҫ������binasciiģ��鿴�����ļ�����ǰ10���ֽڣ�ÿ���������ֽ���ʮ�����Ƶ���ʽ��ʾ��
# -6. �ڶ�ʮ���е�����ʮ���еĹ���������һ�������ļ�����ȡ���������������������ֱ�ӴӴ򿪵��ļ��ж�ȡ������Ϊ�˲��Ե���Ҫ��������ʱд��һ���ļ�����˸�����������ʱ��ǵ�����ָ�뵽�ļ���ͷ����fs.seek(0, 0)��
# -7. ����ʮ���е�����ʮ������Ҫ�ǽ���ȡ����������������AES���ܵõ�������������Ȼ��ر��ļ���
#    ���ˣ��������ǿ������������ָ�������ʱ��Ӱ�����ִ�У����ǻ�Ӱ������print�������һ��ʹ��utf-8���룬�ڶ���ʹ��ascii���룺