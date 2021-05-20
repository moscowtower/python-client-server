import logging

_log_format = f'%(asctime)s - %(levelname)s - %(module)s - %(message)s '
formatter = logging.Formatter(_log_format)

file_handler = logging.FileHandler('log/client.main.log', encoding='utf-8')
file_handler.setFormatter(formatter)

client_logger = logging.getLogger('client.main')

client_logger.addHandler(file_handler)
client_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    client_logger.info('logging test')
    client_logger.warning('KERNEL OVERFLOW!!!!!! joking, logging test')

    client_logger.setLevel(logging.WARNING)

    client_logger.debug('logging test')
    client_logger.critical('logging test')