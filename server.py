# coding=utf-8
import string
import threading
from SocketServer import StreamRequestHandler
from SocketServer import ThreadingMixIn, TCPServer

from common_utils.util_log import log


# define multiThread class
class Server(ThreadingMixIn, TCPServer):
    pass


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
                    # flag to start transmit
                    flag_trans = True
                    print('---*<transmit start.>*---')
                    log.info('{} <start>, transmit begin.'.format(addr))

                    # create new data file
                    start_flag, time_tmp, id_tmp, cnt_tmp = data.split(',')
                    # count of OBD_CMD
                    cnt_cmd = string.atoi(cnt_tmp.split(':')[1])

                    time_data = time_tmp.split(':')[1]
                    id_device = id_tmp.split(':')[1]
                    file_name = './_data/{}_{}.csv'.format(id_device, time_data)
                    data_file = open(file_name, "a+")
                    # data_file.writelines('device: {}, time: {}\n'.format(id_device, time_data))
                    log.info('save data in file: ' + file_name)
                    continue

                if not flag_trans:
                    # if not get '<start>' yet, ignore data.
                    continue

                if data == 'exit' or not data:
                    # client self-close connection
                    print('---*<client exit!>*---')
                    log.info('{} self-closed, client exit!\n'.format(addr))
                    self.finish()
                    break

                elif data == '<end>':
                    # transmit done
                    print('---*<transmit done.>*---')
                    log.info('{} <end>, transmit done.\n'.format(addr))
                    self.finish()
                    break

                else:
                    # send back

                    if len(data.split(',')) - cnt_cmd != 1:
                        data_file.write(data + ',error here.\n')
                    else:
                        data_file.write(data + '\n')

        except Exception, err:
            log.error('connection of client {0} stopped! Error: {1}\n'.format(addr, err.args))

        finally:
            if data_file:
                print('close file')
                data_file.close()
            self.finish()


def start(host, port):
    server = None

    try:

        # bing to Host:port, using TCP
        server = Server((HOST, PORT), StreamHandler)
        server.serve_forever()
        print('---**---Welcome!')
        log.info('---**---listening on {0}:{1}'.format(host, port))
        # # Start a thread with the _server -- that thread will then start one
        # # more thread for each request
        # server_thread = threading.Thread(target=server.serve_forever)
        # # Exit the server thread when the main thread terminates
        # server_thread.daemon = True
        # server_thread.start()
        # print "Server loop running in thread:", server_thread.name
        # threading._sleep(100)

    except Exception, e:
        log.error('service failed to start! Error: {0}\n'.format(e.args))

    finally:

        if server:
            print('---**---Bye!')
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    # HOST, PORT = '202.38.213.72', 80
    # HOST, PORT = '10.0.2.15', 5555
    HOST_GOD = '192.168.1.115'
    HOST, PORT = HOST_GOD, 5555
    start(HOST, PORT)
