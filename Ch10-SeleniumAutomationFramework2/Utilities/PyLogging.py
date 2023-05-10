import logging
from pathlib import Path

# Create a logger object
logger = logging.getLogger(__name__)

# Set the log level to INFO
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('../Logs/example.log')

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter on the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an informational message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')