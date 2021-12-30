# 1. logging module 써보기
import logging

# getLogger() Method로 Logger 객체 생성
logger = logging.getLogger("example") # root logger
logger.info("hello world") # 아무런 로그도 출력되지 않음

# 1.1 logging module config 추가하기
import logging.config

logger_config = {
    "version": 1, # reequired
    "disable_existing_loggers": True, # 다른 Logger를 overriding
    "formatters": {
        "simple": {
            "format": "%(asctime)s | %(levelname)s - %(message)s" # 지정한 포맷 형태로 로그 출력
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        }
    },
    "loggers": {
        "example": {
            "level": "INFO",
            "handlers": ["console"]
        }
    }
}

logging.config.dictConfig(logger_config)
logger_with_config = logging.getLogger("example")
logger_with_config.info("이제 보이죠?")