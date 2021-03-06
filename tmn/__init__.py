import logging

__version__ = '0.2.5'

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger = logging.getLogger('tmn')
logger.addHandler(handler)
logger.setLevel('CRITICAL')
