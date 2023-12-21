# Logging
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

import logging.config

import helper

logging.config.fileConfig("logging/logging.conf", disable_existing_loggers=True)

logger = logging.getLogger("exampleApp")

logger.info("Program started")


# Stack Traces
import traceback

try:
    a = [1, 2, 3]
    value = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())


# Rotating File Handler
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler("logging/app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello, world!")


# Timed Rotating File Handler
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler("logging/timed.log", when="s", interval=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Hello, world!")
    time.sleep(5)
