"""
    使用udp完成：在服务端接受学生信息，将学生信息写入到一个文件中
    每个学生信息占一行
    信息格式： id name age score
    * id(int)
      name(str)
      age(int)
      score(float)
"""
import struct
from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sockfd.bind(('0.0.0.0', 11911))
f = open('class_info.txt', 'a')

while True:
    data, addr_client = sockfd.recvfrom(1024)
    if not data:
        f.close()
        break
    data_st = struct.Struct('i10sif').unpack(data)

    stu_info = "%d %-10s %d %.1f\n"%data_st
    #stu_info = f"{data_st[0]} {data_st[1].decode()} {data_st[2]} {data_st[3]}"

    f.write(stu_info)
    f.flush()
