import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Log\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(meassge)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



