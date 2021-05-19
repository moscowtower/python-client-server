import socket
import time
from jim import *
from options import *
from log.client_log_config import client_logger


def create_presence_msg(user_name, status):
    ts = time.time()
    presence_msg = {
        "action": "presence",
        "time": ts,
        "type": "status",
        "user": {
            "account_name": user_name,
            "status": status
        }
    }
    return presence_msg


def send(args, options_file):
    conf = get_options(args, options_file)
    host = conf['DEFAULT']['HOST']
    port = int(conf['DEFAULT']['PORT'])
    try:
        if not 1024 <= port <= 65535:
            raise ValueError
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except ValueError:
        client_logger.critical('in this universe we use ports 1024-65535')
        sys.exit(1)
    except socket.error as err:
        print("Connection error: {}".format(err))
        sys.exit(2)
    msg = pack(create_presence_msg("Some user", "initial message"))
    sock.send(msg)
    try:
        byte_msg = sock.recv(1024)
        msg = unpack(byte_msg)
        if msg['response'] == 200:
            print(msg)
            client_logger.debug('server answered, status code = 200')
        elif msg['response'] == 402:
            print(msg)
            client_logger.debug('server answered, status code = 402')
        else:
            raise ValueError
    except (ValueError, json.JSONDecodeError):
        client_logger.error('Message decoding error')
    except socket.timeout:
        client_logger.error("Close connection by timeout.")

    if not msg:
        print("No response")

    sock.close()
    print("client close...")


send(sys.argv, "cfg_client.json")