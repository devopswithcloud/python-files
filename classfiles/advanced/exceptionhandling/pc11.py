import logging

logging.basicConfig(level=logging.ERROR,filename='exception.log',
                    format='%(asctime)s -%(levelname)s-%(message)s')
try:
    logging.info(" CHECKING INFO")
    x =1/0 

except ZeroDivisionError:
    logging.exception("Exception occured")
