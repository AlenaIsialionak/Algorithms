from logger import logger

# Configure logging

# logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w',
#                     format='%(asctime)s - %(levelname)s - %(message)s')






def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Called {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


print(add(1, 2))