import sys
import logging


class localLogger:
    def __init__(self):
        self.filename = 'src/logs/files.log'

    def loggerOut(self, uniqueId, msg):
        logging.basicConfig(
            filename=self.filename,
            format='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG
        )
        logging.debug('Request-ID: {} | {}'.format(uniqueId, msg))
