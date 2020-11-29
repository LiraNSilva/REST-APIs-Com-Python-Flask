import logging
import datetime
from pygelf import GelfTcpHandler, GelfUdpHandler, GelfTlsHandler, GelfHttpHandler
#import graypy


class Logger:
    
    def __init__(self,name):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_handler = logging.FileHandler(f"{name}_{date}.log")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        #handler = graypy.GELFTLSHandler('192.168.138.130',12201)
        handler = GelfTcpHandler(host='192.168.138.130', port=12201)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(handler)
        #stream_handler = logging.StreamHandler('employee.log')
        #stream_handler.setFormatter(formatter)
        #logger.addHandler(stream_handler)

    def info(self,mensagem):
        self.logger.info(mensagem)

    def error(self,mensagem):
        self.logger.error(mensagem)