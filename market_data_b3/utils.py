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


def check_status_download(path_log, request_data):
    """Check if the xml has already been downloaded"""
    check = [request_data]
    check_result = []

    with open(path_log, 'r') as f:
        f = f.readlines()

    for line in f:
        for word in check:
            if word in line:
                line = line.replace('\n', '')
                check_result.append(line)

    if len(check_result) == 1:
        # In the first request, the file already existed
        status_download = check_result[0].split('INFO')[1].lstrip()
        if status_download == 'Download success':
            return True
        else:
            return False
    elif len(check_result) > 1:
        # The file didn't exist in the first request so the check_result list has more than one object
        # so I get the status of the last object
        status_download = check_result[-1].split('INFO')[1].lstrip()
        if status_download == 'Download success':
            return True
        else:
            return False
    else:
        return False



