from logger import logging
def  add(a,b):
    logging.debug("Addition function is taking place")
    return a+b
logging.debug("Addition Function has completed")
add(10,15)