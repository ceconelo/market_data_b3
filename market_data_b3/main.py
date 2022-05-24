from request_b3 import RequestB3
from datetime import datetime


def main():
    # Let's pass today's date to the method that will download the file
    _request_data = datetime.today().strftime('%y%m%d')
    # _request_data = '220523'  # Test

    RequestB3(_request_data).start()


if __name__ == '__main__':
    main()
