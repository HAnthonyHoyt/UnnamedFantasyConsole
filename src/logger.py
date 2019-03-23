import json
import logging.config

logger = logging.getLogger('fantasy_console')

try:
    with open("log.json", mode="r") as cfg_file:
        cfg_data = json.loads(cfg_file.read())
        logging.config.dictConfig(cfg_data)
except FileNotFoundError as ex:
    print("Unable to locate log config file")
