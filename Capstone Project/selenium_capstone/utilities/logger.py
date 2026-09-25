import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        reports_folder = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "reports"
        )

        os.makedirs(
            reports_folder,
            exist_ok=True
        )

        log_file = os.path.join(
            reports_folder,
            "automation.log"
        )

        logger = logging.getLogger(
            "SeleniumAutomation"
        )

        if not logger.handlers:

            logger.setLevel(
                logging.INFO
            )

            file_handler = logging.FileHandler(
                log_file
            )

            console_handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

            logger.addHandler(
                console_handler
            )

        return logger