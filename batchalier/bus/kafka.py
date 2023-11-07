import logging

logger = logging.getLogger(__name__)


class KafkaSubmitter:
    """Kafka implementation of the bus job submitter"""

    def __init__(self):
        logger.info("Instantiated")


class KafkaProcessor:
    """Kafka implementation of the bus job processor"""

    def __init__(self):
        logger.info("Instantiated")
