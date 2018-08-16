import traceback
import sys

__author__ = 'Ivan Pobeguts'

if __name__ == '__main__':
    try:
        pass
    except:
        (ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
        print('*** ERROR: type {} value {}'.format(ErrorType, ErrorValue))
        traceback.print_tb(ErrorTB)

