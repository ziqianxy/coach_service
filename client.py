# coding=utf-8
import socket

from common_utils.util_log import log

HOST_VM = '10.0.2.15'
HOST_GOD = '192.168.1.115'
LOCALHOST = 'localhost'
HOST_1001 = '125.217.226.161'
HOST_SCUT = '202.38.213.72'

HOST = HOST_GOD
PORT = 5555

s = None
try:
    # connect to _server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # 定义socket类型，网络通信，TCP
    s.connect((HOST, PORT))       # 要连接的IP与端口
    log.info('connected to {0}:{1}'.format(HOST, PORT))
    try:
        # 循环接收来自客户端的命令
        count = 0
        while True:
            cmd = raw_input("> ")       # 与人交互，输入命令
            # cmd = 'test'
            if len(cmd) == 0:
                continue
            if cmd.lower() == 'exit':
                s.sendall('exit')
                log.info('<self-exit>')
                print('Bye!')
                break
            # 想服务器端发送输入的命令
            cmd_line = cmd + '\n'
            s.sendall(cmd_line)
            # 获取接收的数据
            data = s.recv(1024)
            data = data.decode('GB2312').encode('utf-8')
            count += 1
            log.debug('Ask_{0}: {1}, Reply: {2}'.format(count, cmd, data))

    except Exception, e:
        log.error('Error: connect aborted! Args: {0}\n'.format(e.args))

except Exception, e:
    log.error('connect failed! Args: {0}\n'.format(e.args))

finally:
    if s is not None:
        s.close()   # 关闭连接
        log.info('*-----* Close Client.\n')
