import os
import os.path
import subprocess
import webbrowser

import requests as requests


def prep_directory(subdir):
    """
    Creates subdirectory 'subdir' of lolcat main directory if it doesn't exist
    Ensures the directory is empty by deleting files if necessary
    :param subdir:
    :return: 0 for success, 1 for fail
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    cat_dir = os.path.join(base_dir, subdir)
    if not os.path.exists(cat_dir):
        print('Creating cat directory: {}'.format(cat_dir))
        os.mkdir(cat_dir)

    # Ensure directory is empty
    for root, dirs, files in os.walk(cat_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    return cat_dir


def download_pics(num, subdir):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    for i in range(num):
        print('Getting cat number {}'.format(i))
        r = requests.get(url)
        # This url works via a redirect.
        # Occasionally, not redirected to a jpg file, so need to check the file extension
        file_ext = r.url.split('/')[-1].split('.')[-1]
        with open(os.path.join(subdir, 'cat_{}.{}'.format(i, file_ext)), 'wb') as f:
            f.write(r.content)


def display_pics(subdir):
    """Opens the contents of subdir using platform appropriate application"""
    for root, dirs, files in os.walk(subdir):
        for file in files:
            webbrowser.open(os.path.join(subdir, file), new=2)
