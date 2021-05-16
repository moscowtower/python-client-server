from socket import *
from options import *
from jim import *
from log.server_log_config import server_logger


def run(args, options_file):
    sock = socket(AF_INET, SOCK_STREAM)  # creates tcp socket
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])
    try:
        if not 1024 <= port <= 65535:
            raise ValueError
        sock.bind(('', port))
        sock.listen(5)  # server is waiting for requests;
        print("sever is running")
    except ValueError:
        server_logger.critical('in this universe we use ports 1024-65535')
        sys.exit(1)
    while True:
        client, addr = sock.accept()
        data = client.recv(1000000)
        if unpack(data):
            print('Message: ', unpack(data), ', was sent by client: ', addr)
            msg = status_200()
            client.send(msg)
            client.close()
        else:
            print('Bad format')


run(sys.argv, "cfg_server.json")