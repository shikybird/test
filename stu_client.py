"""
    使用udp完成：客户端不断录入学生信息
    将其发送到服务端
    信息格式： id name age score
        * id(int)
          name(str)
          age(int)
          score(float)
"""
import struct
from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ('127.0.0.1', 11911)

while True:
    data = input('请输入学生信息： ').split(' ')
    if not data:
        break
    info_st = struct.Struct('i10sif').pack(int(data[0]), data[1].encode(), int(data[2]), float(data[3]))
    print(info_st)
    sockfd.sendto(info_st, server_addr)

sockfd.close()
