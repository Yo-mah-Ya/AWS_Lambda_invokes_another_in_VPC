# -*- encoding:utf-8 -*-
import json
from logging import getLogger, StreamHandler, DEBUG
import os


# logger setting
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(os.getenv("LogLevel", DEBUG))
logger.addHandler(handler)
logger.propagate = False


def lambda_handler(event, context)-> dict:
    logger.info(json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"})
    }
