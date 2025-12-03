# Development utilities
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def log_message(msg):
    logger.info(msg)
