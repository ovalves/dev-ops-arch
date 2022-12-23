import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    filename="logs/producer.log",
    filemode="w",
)

log = logging.getLogger()
log.setLevel(logging.INFO)