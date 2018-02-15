# -*- coding: utf-8 -*-
import logging
import sys
from logstash_async.handler import AsynchronousLogstashHandler
from os import environ

host = 'satoh.nazwa.pl'
port = 6240

class Logger:
    def __init__(self):
        self.extra = { 'player': environ["MINECRAFT_PLAYER_NAME"]}
        self.logger = logging.getLogger('python-logstash-logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(AsynchronousLogstashHandler(host, port, database_path='logstash_test.db'))

    def info(self, data):
        self.logger.info(data, extra = self.extra)


if __name__ == "__main__":
    environ["MINECRAFT_PLAYER_NAME"] = "Spock"
    logger = Logger()
    logger.info("sample log message")
