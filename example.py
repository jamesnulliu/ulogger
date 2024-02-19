import logging

import mylogger
mylogger.setup()


def test():
    logger = logging.getLogger("root")
    logger.debug("This is a debug message.", extra={'extra_info': 'Hello!'})
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    try:
        1 / 0
    except Exception as e:
        logger.exception("An exception was thrown!")


if __name__ == '__main__':
    test()