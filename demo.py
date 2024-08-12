from us_visa.logger import logger
from us_visa.exception import USvisaException
import sys

#logger.info("welcome to our custome log")

try:
    a= 2/0
except Exception as e:
    raise USvisaException(e, sys)
