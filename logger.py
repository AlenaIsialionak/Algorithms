import logging

# create a logger
logger = logging.getLogger('my_logger')

# Configure the logger
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('my_log.loG')

# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s  - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log messages
logger.info('This is an informational message')
logger.warning('This is warning message')
logger.error('This is an error message')
