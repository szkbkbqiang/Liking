# -*- coding: utf-8 -*-
import json
from Crypto import Random
from Crypto.Cipher import AES
import numpy as np
import AESUtil
import package
import data
import time


def Equipment_registration(tcpClientSocket,data_register):
    #设备注册0x65
    #data_register = data.register()
    # for letter in data_register:
        text = json.dumps(data_register)
        iv = Random.new().read(AES.block_size)
        #aes = AESUtil.AESUtil('keykeykeykeykey1')  # 初始化密钥 和 iv
        aes = AESUtil.AESUtil('keykeykeykeykey1', iv)  # 初始化密钥 和 iv
        data_aes = iv + aes.encrypt(text)  # 加密]
        cmd=0x65
        t = (int(time.time()))
        send_package=package.package(data_aes,cmd,t)
        # 转成16进制
        data_hex = np.array(bytearray(send_package))
        tcpClientSocket.send(data_hex)  # 发送数据
        def recv_size(the_socket):
            # 先读取4个字节，赋值给l，然后根据l在读取l长度字节
            recv_size = the_socket.recv(4)
            l = int.from_bytes(recv_size, byteorder='big', signed=True)
            sock_data = the_socket.recv(l)
            return sock_data
        #接收数据
        feedback = recv_size(tcpClientSocket)
        msg_id = package.analysis(feedback)[0]  # 获取msg_id
        print('feedback返回的msg_id:', msg_id)
        analysis_package = package.analysis(feedback)[1]  # 获取解析数据包
        print('feedback解析数据包：', analysis_package.decode('utf-8'))
        assert str(t) in analysis_package.decode('utf-8')
        recvData = recv_size(tcpClientSocket)
        msg_id=package.analysis(recvData)[0]#获取msg_id
        print('注册返回的msg_id:',msg_id)
        analysis_package=package.analysis(recvData)[1]#获取解析数据包
        print('注册解析数据包：',analysis_package)

        #############返回feedback###################
        feedback = [{
            'msg_id': msg_id,  # 消息ID int64 此feedback包是针对该msg_id的回包
        }]
        text = json.dumps(feedback)
        iv = Random.new().read(AES.block_size)
        aes = AESUtil.AESUtil('keykeykeykeykey1', iv)  # 初始化密钥 和 iv
        data_aes = iv+aes.encrypt(text)  # 加密

        # #####返回包头#####
        t = (int(time.time()))
        result_feedback=package.package(data_aes,0x6F,t)
        # 转成16进制
        data_hex = np.array(bytearray(result_feedback))
        tcpClientSocket.send(data_hex)  # 发送数据
def business_function(tcpClientSocket,number):

    #业务功能
    bracelet = 10000000
    while bracelet < 10000000+number:
        bracelet += 1
        data_bracelet = data.bracelet_id(bracelet)

        text = json.dumps(data_bracelet)
        print('发送的业务数据',text)
        iv = Random.new().read(AES.block_size)
        aes = AESUtil.AESUtil('keykeykeykeykey1',iv)  # 初始化密钥 和 iv
        data_aes = iv+aes.encrypt(text)  # 加密
        cmd=0x70
        t = (int(time.time()))

        send_package=package.package(data_aes,cmd,t)
        # 转成16进制
        data_hex = np.array(bytearray(send_package))
        tcpClientSocket.send(data_hex)  # 发送数据
        def recv_size(the_socket):
            # 先读取4个字节，赋值给l，然后根据l在读取l长度字节
            recv_size = the_socket.recv(4)
            l = int.from_bytes(recv_size, byteorder='big', signed=True)
            sock_data = the_socket.recv(l)
            return sock_data
        #接收数据
        feedback = recv_size(tcpClientSocket)
        msg_id = package.analysis(feedback)[0]  # 获取msg_id
        print('feedbackmsg_id:', msg_id)
        analysis_package = package.analysis(feedback)[1]  # 获取解析数据包
        print('feedback解析数据包：', analysis_package)
        assert str(t) in analysis_package.decode('utf-8')

        recvData = recv_size(tcpClientSocket)
        msg_id=package.analysis(recvData)[0]#获取msg_id
        print('业务返回的msg_id:',msg_id)
        analysis_package=package.analysis(recvData)[1]#获取解析数据包
        print('业务解析数据包：',analysis_package)


        #############返回feedback###################
        feedback = [{
            'msg_id': msg_id,  # 消息ID int64 此feedback包是针对该msg_id的回包
        }]
        text = json.dumps(feedback)
        iv = Random.new().read(AES.block_size)
        aes = AESUtil.AESUtil('keykeykeykeykey1', iv)  # 初始化密钥 和 iv
        data_aes = iv + aes.encrypt(text)  # 加密

        # #####返回包头#####
        t = (int(time.time()))
        result_feedback=package.package(data_aes,0x6F,t)
        # 转成16进制
        data_hex = np.array(bytearray(result_feedback))
        tcpClientSocket.send(data_hex)  # 发送数据

def heart_beat(tcpClientSocket,heartbeat):
    #心跳包
    #data_1 = data.heartbeat()
        # 心跳包0x64


    # for letter in data_register:
        text = json.dumps(heartbeat)
        iv = Random.new().read(AES.block_size)
        aes = AESUtil.AESUtil('keykeykeykeykey1', iv)  # 初始化密钥 和 iv
        data_aes = iv+aes.encrypt(text)  # 加密
        cmd=0x64
        t = (int(time.time()))
        send_package=package.package(data_aes,cmd,t)
        # 转成16进制
        data_hex = np.array(bytearray(send_package))
        tcpClientSocket.send(data_hex)  # 发送数据
        def recv_size(the_socket):
            # 先读取4个字节，赋值给l，然后根据l在读取l长度字节
            recv_size = the_socket.recv(4)
            l = int.from_bytes(recv_size, byteorder='big', signed=True)
            sock_data = the_socket.recv(l)
            return sock_data
        #接收数据
        # feedback = recv_size(tcpClientSocket)
        recvData = recv_size(tcpClientSocket)
        msg_id=package.analysis(recvData)[0]#获取msg_id
        print('心跳返回的msg_id:',msg_id)
        analysis_package=package.analysis(recvData)[1]#获取解析数据包
        print('心跳解析数据包：',analysis_package)






# print('关闭 socket!')