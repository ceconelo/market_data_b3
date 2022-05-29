import requests
import zipfile
import logging
import os, sys

from io import BytesIO

from utils import delete_zip_files, unzip_file

""" This module is responsible for connecting to the B3 website and downloading the file 
    BVBG.186.01 - Simplified Price Report - Equities. 
    
    1. We connect to the base url to get the cookies that the server returns. 
    2. We make a request at the address that answers the file we need, passing as a parameter the name of the file 
    which is formed by SPRE + Date.
    3. We extract the zipped file.
    4. We deleted the zip file. """


class RequestB3:

    def __init__(self, request_data):
        self._request_data = request_data

        self._url_base = 'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico' \
                         '/boletins-diarios/pesquisa-por-pregao/pesquisa-por-pregao/ '
        self._url_download_zip = f'https://www.b3.com.br/pesquisapregao/download?filelist=SPRE{self._request_data}.zip'

        self._path_file = f'output/'
        self._zipfile_name = self._url_download_zip.split('=')[1]

        self.web = requests.session()
        self.web.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                         'Chrome/101.0.4951.64 Safari/537.36 '

    def _download_xml(self, cookies):
        print('[Info] Searching for the zipped file.')
        response = self.web.get(self._url_download_zip, cookies=cookies, stream=True)
        if response.status_code == 200:
            if len(response.content) > 22:  # If no file is found, the server returns a string of 22 characters
                try:
                    print('[Info] Downloading file.')
                    file = zipfile.ZipFile(BytesIO(response.content))
                    file.extractall(self._path_file)
                    logging.info('Download success')
                except BaseException as err:
                    print('[Error] Unable to download and save file.')
                    logging.info('Download failed')
                    print(err)
                    sys.exit(os.EX_OSFILE)
            else:
                print(f'[Info] No files were found for that date: {self._request_data}')
                logging.info('Download failed')
                sys.exit(os.EX_OK)

        else:
            print('Error:')

    def start(self):
        print('[Info] Accessing b3 website')
        base_page = self.web.get(url=self._url_base)
        self._download_xml(base_page.cookies)
        unzip_file(path_zip=self._path_file, zip_name=self._zipfile_name)
        delete_zip_files(path_zip=self._path_file)
