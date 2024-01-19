import enum
import logging
from logging.handlers import RotatingFileHandler
import sys

from .constants import FW_APP_NAME, DEFAULT_LOG_FORMAT


class LogLevel(enum.IntEnum):
    debug = logging.DEBUG
    info = logging.INFO
    warning = logging.WARNING
    error = logging.ERROR
    fatal = logging.FATAL
    critical = logging.CRITICAL


class Logger:
    def __init__(
            self,
            logger_name: str,
            *,
            level: LogLevel = LogLevel.info,
            log_format: str = DEFAULT_LOG_FORMAT,
            to_file: bool = False,
            log_file_size: int = 5000000,
            log_file_count: int = 5,
    ) -> None:
        if not logger_name:
            raise ValueError('`logger_name` is required')

        self.__logger = logging.getLogger(logger_name)

        self.__logger.setLevel(level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(log_format))
        self.__logger.addHandler(handler)

        if to_file:
            handler = RotatingFileHandler(
                f'{logger_name}.log',
                maxBytes=log_file_size,
                backupCount=log_file_count,
            )
            handler.setFormatter(logging.Formatter(log_format))
            self.__logger.addHandler(handler)

        self.info('Start logging')

    def debug(self, msg, *args, **kwargs):
        self.__logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.__logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.__logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.__logger.critical(msg, *args, **kwargs)


logger = Logger(FW_APP_NAME)
