import json
import logging.config

with open('configs/logging.json', 'rt') as f:
    logging_config = json.load(f)

logging.config.dictConfig(logging_config)
logger = logging.getLogger("flask.app")
payload_logger = logging.getLogger("payload_logger")
