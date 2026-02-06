from Visa.logger import logging
from Visa.exception import USvisaException
import sys 


# logging.info("this is a test file from demo.py")

try:
    a =1/0
except Exception as e:
    raise USvisaException(e,sys)
