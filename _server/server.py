# coding=utf-8
import socket

from server_socket import HOST, PORT

from _server.server_thread import ServerThread
from common_utils.util_log import log

id_client = 0
socket_server = None
flag = True
thread_list = []

try:
    # bing to Host:port, using TCP
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 定义socket类型，网络通信，TCP
    socket_server.bind((HOST, PORT))   # 套接字绑定的IP与端口
    socket_server.listen(3)         # 开始TCP监听
    flag = True
    print('---**---Welcome!')
    log.info('---**---listening on {0}:{1}'.format(HOST, PORT))

    try:
        while flag:
            id_client += 1
            # 接受TCP连接，并返回新的套接字与IP地址
            socket_z, address_z = socket_server.accept()
            # 开启新线程，并传递socket，id号码自增1
            server_thread = ServerThread(id_client, socket_z, address_z)
            server_thread.start()
            thread_list.append(server_thread)
    except Exception, e:
        log.error('connection od _client {0} failed! Error: {1}'.format(id_client, e.args))

except Exception, e:
    flag = False
    log.error('service failed to start! Error: {0}'.format(e.args))

finally:
    print('---**---Bye!')
    if socket_server is not None:
        socket_server.close()
    for thread in thread_list:
        if thread.isAlive():
            print thread
