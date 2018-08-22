# -*- coding: UTF-8 -*-

import socket
import Package_collection
import data
import json
import random

# 创建套接字
tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('socket---%s' % tcpClientSocket)
# 链接服务器
serverAddr = ('120.79.101.51', 37919)
tcpClientSocket.connect(serverAddr)
print('socket连接成功!')



# 设备注册0x65
def data_register(device_id):
    register = [{
        'device_id':device_id,  # 设备ID string
        'gateway_id': '',  # 网关设备ID string
        'device_name': '力量区人感',  # 设备名称 string
        'device_type': 26,  # 无硬件迭代不扩展 int8
        'control_num': '3',  # 设备控制点数，如开关下辖三路灯。 Int32
        'online_status': '0',  # 设备在线状态，0离线 1在线 int8
        'battery_status': 1,  # 设备电量状态，0不足 1充足，无电量属性设备默认为1 int8
        'device_status': 0,  # 设备运行状态，0关，1开，2暂停 int8
        'bluetooth_mac': 'AABBCCDDEEFFGG',  # 蓝牙mac地址
        'ethernet_mac': 'GGFFEEDDCCBBAA'}  # 以太网mac地址
    ]
    return register

device_id=random.randint(100000,100099)
data_register = data_register(device_id)


Package_collection.Equipment_registration(tcpClientSocket,data_register)#设备注册0x65
#用户数量
number=1
Package_collection.business_function(tcpClientSocket,number)#业务功能

#Package_collection.heart_beat()#心跳包

def recv_size(the_socket):
    # 先读取4个字节，赋值给l，然后根据l在读取l长度字节
    recv_size = the_socket.recv(4)
    l = int.from_bytes(recv_size, byteorder='big', signed=True)
    sock_data = the_socket.recv(l)
    return sock_data

while True:
    #心跳
    heartbeat = [{
        'device_id': device_id,  # 设备ID string
    }]
    Package_collection.heart_beat(tcpClientSocket,heartbeat)  # 心跳包
    recvData = recv_size(tcpClientSocket)
    if not recvData:
        break
    print('后续接收到的数据： ', recvData)

# 关闭套接字
tcpClientSocket.close()
print('关闭 socket!')



# while True:
#
#     #接收数据
#     recvData = recv_size(tcpClientSocket)
#     #打印接收到的数据
#     print('接收到的数据： ', recvData)
#     #接收后再次发送
#     #tcpClientSocket.send(data)#发送数据




