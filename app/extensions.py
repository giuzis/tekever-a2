import os
import logging
from logging.handlers import TimedRotatingFileHandler

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Log configuration
LOG_PATH = APP_ROOT+"/logs"

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(message)s", level=logging.DEBUG
)

log = logging.getLogger()
handler = TimedRotatingFileHandler(
    LOG_PATH+"/events.log", when="midnight", encoding="utf-8", backupCount=12
)
formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)