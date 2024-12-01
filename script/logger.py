import logging 
import os
from datetime import datetime

file_name = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
log_path = os.path.join(os.getcwd(),'logs',file_name)

os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,file_name)
print(log_file_path)


logging.basicConfig(level = logging.INFO,
                    filename=log_file_path,
                    format='[%(asctime)s] %(filename)s %(lineno)d %(name)s -%(levelname)s - %(message)s'
                    )

logger = logging.getLogger('My Logger')
fmt = '[%(asctime)s] %(filename)s %(lineno)d %(name)s -%(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)


StreamHandler = logging.StreamHandler()
StreamHandler.setFormatter(formatter)
logger.addHandler(StreamHandler)


