# -*- encoding:utf-8 -*-
import base64
import json
from logging import getLogger, StreamHandler, DEBUG
import os
import boto3

# logger setting
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(os.getenv("LogLevel", DEBUG))
logger.addHandler(handler)
logger.propagate = False

lambda_client = boto3.client("lambda")
FUNCTION_NAME = os.environ["TARGET_FUNCTION"]


def lambda_handler(event, context)-> dict:
    logger.info(json.dumps(event))

    lambda_client.invoke(
        FunctionName = FUNCTION_NAME,
        InvocationType = 'RequestResponse',
        LogType = 'Tail',
        Payload = json.dumps({"message": "test-data"}).encode("utf-8")
    )


    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"})
    }
