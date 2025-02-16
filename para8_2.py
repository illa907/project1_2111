import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_para8_2.log",
                    filemode="w",
                    format="We have next logging massage: %(asctime)s%(levelname)s - %(message)s")


try:
    print(10/0)
except Exception:
    logging.exception("exception")
