import logging

__all__ = ["info", "warn", "error", "debug"]

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

LOGGER = None


def get_logger():
    global LOGGER
    if LOGGER:
        return LOGGER
    LOGGER = logging.getLogger("machine-learning")
    fmt = logging.Formatter(fmt=LOG_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(fmt)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
    return LOGGER


def error(msg, *args, **kwargs):
    get_logger().error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    get_logger().warning(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    get_logger().info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    get_logger().debug(msg, *args, **kwargs)


