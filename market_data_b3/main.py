from request_b3 import RequestB3
from utils import check_status_download
from datetime import datetime

import logging
PATH_LOG = '/home/drakon/Documents/PROJETOS/market_data_b3/market_data_b3/output/download.log'

logging.basicConfig(
    filename=PATH_LOG,
    filemode='a',
    format='%(asctime)s - %(levelname)s %(message)s',
    datefmt='%y%m%d',
    level=logging.INFO
)


def main():
    # Let's pass today's date to the method that will download the file
    _request_data = datetime.today().strftime('%y%m%d')
    # _request_data = '220525'  # Test

    if not check_status_download(path_log=PATH_LOG, request_data=_request_data):
        RequestB3(_request_data).start()
    else:
        print('[INFO] The xml referring to the informed date has already been downloaded.')


if __name__ == '__main__':
    main()
