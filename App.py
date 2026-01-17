import logging 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers = [
                        logging.FileHandler('app.log'),
                        logging.StreamHandler() 
                                ]
)

logging = logging.getLogger('ArithmeticApp')

def add(a, b):
    result = a + b
    logging.debug(f'Adding {a} and {b} to get {result}')
    return result

def subtract(a, b):
    result = a - b
    logging.debug(f'Subtracting {b} from {a} to get {result}')
    return result

def multiply(a, b):
    result = a * b
    logging.debug(f'Multiplying {a} and {b} to get {result}')
    return result

def divide(a, b):
    try:
        result = a / b
        logging.debug(f'Dividing {a} by {b} to get {result}')
        return result
    except ZeroDivisionError:
        logging.error('Attempted to divide by zero')
        return None
    
add(10, 5)
subtract(10, 5)     
multiply(10, 5)
divide(10, 0)
