# coding=utf-8
import commands
import threading

from common_utils.util_log import log


class ServerThread(threading.Thread):
    def __init__(self, thread_id, client_socket, client_address):
        threading.Thread.__init__(self)
        self.id = thread_id
        self.socket = client_socket
        self.address = client_address
        log.info('***---_client connected, id:{0}, address: {1}:{2}'.format(self.id, self.address[0], self.address[1]))

    def run(self):
        try:
            while True:
                # 获取把接收的数据
                print('make file')
                # self.socket.connect()
                socket_file = self.socket.makefile()
                print socket_file
                in_msg = socket_file.readlines()
                print in_msg
                # in_msg = self.socket.recv(1024)
                if len(in_msg) == 0:
                    # 忽略空信息
                    continue
                if in_msg.lower() == 'exit':
                    # 客户端主动退出处理
                    log.info('*----* _client{0} disconnected self.'.format(self.id))
                    self.socket.close()
                    break

                # 客户端消息处理
                # self.cmd_handler(in_cmd)
                self.msg_handler(in_msg)

        except Exception, e:
            log.error('*----* _client{0} disconnected. Exception Args: {1}'.format(self.id, e))
        finally:
            if self.socket is not None:
                self.socket.close()

    def msg_handler(self, msg):

        log.info('client_id: {0},msg: \n{1}'.format(self.id, msg))
        if msg == 'test':
            self.socket.sendall('test back.')
            log.info('[test]')
        elif msg == '<end>':
            self.socket.sendall('Done.')
            log.info('<transmit end>')
        else:
            pass

    def cmd_handler(self, in_cmd):
        # commands.getstatusoutput 执行系统命令（即shell命令）
        # 返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
        cmd_status, cmd_result = commands.getstatusoutput(in_cmd)
        # cmd_result = cmd_result.replace('\n', '').replace('\r\n', '')
        log.info('client_id: {0},command: {1}, status: {2}'.format(self.id, in_cmd, cmd_status))
        if len(cmd_result.strip()) == 0:
            # 如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
            self.socket.sendall('Done.')
            log.info('result: Done.')
        else:
            # 否则就把结果发给对端（即客户端）
            self.socket.sendall(cmd_result + '\n')
            out_result = cmd_result.replace('\n', '').replace('\r\n', '')
            out_result = out_result.decode('GB2312').encode('utf-8')
            log.info('result:{0}'.format(out_result))
