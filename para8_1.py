import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_para8_1",
                    filemode="a",
                    format="We have next logging massage: %(asctime)s%(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")