import logging

logger = logging.getLogger(__name__)

# Don't propagate to the root logger
# logger.propagate = False

logger.info("Hello from helper.py")

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logging/file.log")

# set the log level for the handlers
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# set the format for the handlers
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("This is a warning")
logger.error("This is a error")
