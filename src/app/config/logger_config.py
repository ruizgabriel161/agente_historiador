from pygrlogging.logging_config import LoggingConfig

_config_log = LoggingConfig(config_file="logging.json", logs_dir="logs")

def get_logger(name:str):
    return _config_log.get_logger(name=name)


