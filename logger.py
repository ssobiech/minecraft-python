# -*- coding: utf-8 -*-
import logging
from logging.config import fileConfig
from os import environ


class Logger:
    def __init__(self):
        fileConfig('logging.conf', disable_existing_loggers=True)
        self.logger = logging.getLogger()
        self.extra = {'player': environ["MINECRAFT_PLAYER_NAME"]}

    def info(self, data):
        self.logger.info(data, extra = self.extra)


if __name__ == "__main__":
    environ["MINECRAFT_PLAYER_NAME"] = "souza539"
    logger = Logger()
    logger.info("sample log message")
