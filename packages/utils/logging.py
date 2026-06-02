import logging

def configure_logging(level='INFO'):
    logging.basicConfig(level=getattr(logging, level.upper()))