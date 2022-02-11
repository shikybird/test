"""
    http server 1.0
"""

from socket import *


def request(connfd):
    # 获取请求并将请求内容提取出来
    data = connfd.recv(1024)
    # 防止浏览器异常退出
    if not data:
        return
    list_temp = data.decode().split(' ')
    info = list_temp[1]

    # 判断是 / 则返回index.html 不是则返回404
    if info == '/':
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...</h1>"

    connfd.send(response.encode())


sockfd = socket()

sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sockfd.bind(('127.0.0.1', 11911))

sockfd.listen(3)

while True:
    connfd, adr = sockfd.accept()
    request(connfd)
    connfd.close()

