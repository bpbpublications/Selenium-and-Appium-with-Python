import inspect
import logging
import allure


def appLogger():
    logName = inspect.stack()[1][3]

    logger = logging.getLogger(logName)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("./Logs/ApplicationLog.log")

    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
