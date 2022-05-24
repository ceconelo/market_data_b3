import zipfile
import glob
import os


def unzip_file(path_zip, zip_name):
    """unzip files and delete original zip files"""
    try:
        print('[Info] Extracting files')
        with zipfile.ZipFile(path_zip + zip_name, "r") as zip_ref:
            zip_ref.extractall(path_zip)
    except BaseException as err:
        print('[Error] An error occurred while trying to extract the file.')
        print(err)
        exit(1)


def delete_zip_files(path_zip):
    """Delete the zip file"""
    try:
        for zippath in glob.iglob(os.path.join(path_zip, '*.zip')):
            os.remove(zippath)
        print('[Info] Deleted zip files.')
    except BaseException as err:
        print('[Error] An error occurred while trying to delete the zipped files.')
        print(err)

