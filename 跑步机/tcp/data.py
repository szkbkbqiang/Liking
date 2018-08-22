# -*- coding: UTF-8 -*-
import json

def register():
    #设备注册0x65
    register = [{
    'device_id': 'a000000100010001',#设备ID string
    'gateway_id': '',#网关设备ID string
    'device_name':'力量区人感', # 设备名称 string
    'device_type': 26, # 无硬件迭代不扩展 int8
    'control_num': '3',  # 设备控制点数，如开关下辖三路灯。 Int32
    'online_status': '0',  # 设备在线状态，0离线 1在线 int8
    'battery_status': 1,  # 设备电量状态，0不足 1充足，无电量属性设备默认为1 int8
    'device_status': 0,# 设备运行状态，0关，1开，2暂停 int8
    'bluetooth_mac':'AABBCCDDEEFFGG',  # 蓝牙mac地址
    'ethernet_mac':'GGFFEEDDCCBBAA'}#以太网mac地址
    ]
    return register
def Report():
    #设备上报0x68
    Report = [
    {
    'device_id ': 'a000000100010001', #设备ID string
    'gateway_id' : '', #网关设备ID string
    'device_name':'AB门',#设备名称 string
     'device_type' : 1, #无硬件迭代不扩展 int8
     'control_num' : 10, #设备控制点数，如开关下辖三路灯。 Int32
     'online_status' : 1, #设备在线状态，0离线 1在线 int8
    'battery_status' : 1, #设备电量状态，0不足 1充足，无电量属性设备默认为1 int8
    'device_status' : 1 #设备运行状态，0关，1开，2暂停 int8
         }]
    return Report
def feedback():
    #feedback包0x65
    feedback=[{
    'msg_id' : 10000000000, #消息ID int64 此feedback包是针对该msg_id的回包
    }]
    return feedback
def heartbeat():
    #心跳包0x64
    heartbeat=[{
    'device_id' : '10000000000', #设备ID string
    }]
    return heartbeat
def time():
    #获取时间戳:0x66
    time={''}
    return time
def update():
    #程序更新:0x66
    update=[{
    "url":"www.likingfit.com",#更新包url string
    "app_md_5":"959872074132d638c39831a4a70faae16720486a", #软件md5摘要 string
    "app_size":256347899, #更新包大小，单位字节 int64
     }]
    return update



#业务数据--Cmd：0x70

#上报手环ID


import sql
def bracelet_id(bracelet):

    Bracelet_id={
      "cmd":1,
      'data':{
        'bracelet_id':sql.query(bracelet),# 手环ID int32
        'bracelet_type':1,#手环类型 1普通手环   2 cpu卡手环  int8
             },
                }
    return Bracelet_id
# bracelet = 10000000
# bracelet += 1
# d = bracelet_id(bracelet)
# print(d)




#上报用户手环鉴权
authentication={
  "cmd":3,
  'data':{
'cpu_key':'tyui45678v', #鉴权key
'bracelet_id':'a000000000001',#手环ID int32
  },
}



#获取会员列表
user={
  "cmd":5,
  'data':{
    'sync_id':0,#上次同步最大ID unsigned int32
  },
}

#上报离线数据
Off_line={
  "cmd":7,
  'data':{
'logs':[
  {
    'bracelet_id':26543212345,#手环ID unsigned int16
    'auth_status':1,# 鉴权结果 0成功 10001失败码 int32
    'auth_type':1,#鉴权类型 1 rfid手环 2 cpu手环  3 蓝牙 int8
    'auth_time':1541454377,#鉴权时间 int16
  }
        ]
         },
        }
#同步门禁设备信息
equipment={
  "cmd":9,
  'data':{
    'software_version':'',# 设备软件版本号
    'hardware_version': '',  # 设备硬件版本号
    'iccid': 1,  # 设备使用的物联网卡ID（如果没使用物联网卡可为空）
    'net_type': 1,  # 设备入网方式: 1有线网  2 wifi
  }
}

#上报异常信息
abnormal={
  "cmd":10,
  'data':{
    'exception':'',#异常信息用于售后维保
  }
}

#上报蓝牙传输信息
Bluetooth={
  "cmd":11,
  'data':{
    'data':'',# 通过蓝牙收到的信息 string
  }
}
# def business():
#     #所有的业务
#     business = (update,authentication,user,Off_line,equipment,abnormal,Bluetooth)
#     #print(data)
#     return business

    # import json
    # json = json.dumps(data[0])
    # print(json)
