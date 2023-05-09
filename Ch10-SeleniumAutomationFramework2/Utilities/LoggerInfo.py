import logging
from pathlib import Path


class LogInfo:
    @staticmethod
    def logGen():
        path = Path(__file__).parent.parent.joinpath('Logs/test.log')
        logging.basicConfig(filename=path, level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        return logging.getLogger()
