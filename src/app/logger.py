import sys
import os
import logging
from logging import StreamHandler, Formatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(Formatter(fmt='["%(asctime)s - [%(levelname)s] - file:%(filename)s, func:%(funcName)s, line:%(lineno)d. %(message)s"]'))


logger.addHandler(handler)
