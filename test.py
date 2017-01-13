# coding=utf-8
import string
import threading
from SocketServer import StreamRequestHandler
from common_utils.util_log import log

class StreamHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        cur_thread = threading.current_thread()
        log_buffer = "Got connection from {}, {}".format(cur_thread.name, self.client_address)
        log.info(log_buffer)

        flag_trans = False
        data_file = None
        cnt_cmd = 0
        try:
            while True:
                data = self.rfile.readline().strip()
                if data.startswith('<start>'):
                    flag_trans = True
                    log.info('{} <start>, transmit begin.'.format(addr))
                    start_flag, time_tmp, id_tmp, cnt_tmp = data.split(',')
                    cnt_cmd = string.atoi(cnt_tmp.split(':')[1])
                    time_data = time_tmp.split(':')[1]
                    id_device = id_tmp.split(':')[1]
                    file_name = './_data/{}_{}.csv'.format(id_device, time_data)
                    data_file = open(file_name, "a+")
                    log.info('save data in file: ' + file_name)
                    continue
                if not flag_trans:
                    continue
                if data == 'exit' or not data:
                    log.info('{} self-closed, client exit!\n'.format(addr))
                    self.finish()
                    break
                elif data == '<end>':
                    log.info('{} <end>, transmit done.\n'.format(addr))
                    self.finish()
                    break
                else:
                    data_file.write(data + '\n')
        except Exception, err:
            log.error('connection of client {0} stopped! Error: {1}\n'.format(addr, err.args))

        finally:
            if data_file:
                print('close file')
                data_file.close()
            self.finish()
