import logging
import logging.handlers


log_info_file = "info.log"

def get_logger(log_file):
    logger = logging.getLogger("inject")
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelno)s - %(funcName)s- %(message)s' 
    hdlr = logging.basicConfig(filename=log_file, level=logging.DEBUG, format=fmt)
    return logger
