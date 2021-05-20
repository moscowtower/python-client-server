import logging
from logging.handlers import TimedRotatingFileHandler

_log_format = f'%(asctime)s - %(levelname)s - %(module)s - %(message)s '
formatter = logging.Formatter(_log_format)

file_handler = logging.FileHandler("log/server.main.log", encoding='utf-8')
file_handler.setFormatter(formatter)

time_rotating_handler = TimedRotatingFileHandler("log/server.main.log", when='midnight', interval=1,
                                                 backupCount=7, encoding='utf-8')
time_rotating_handler.setFormatter(formatter)

server_logger = logging.getLogger('server.main')

server_logger.addHandler(time_rotating_handler)
server_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    server_logger.info('logging test')
    server_logger.warning('logging test')

    server_logger.setLevel(logging.WARNING)

    server_logger.debug('logging test')
    server_logger.critical('logging test')