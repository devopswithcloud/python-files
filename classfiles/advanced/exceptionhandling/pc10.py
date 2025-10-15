import logging

logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='w',
                    format='%(asctime)s -%(levelname)s-%(message)s')

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is a critical error")