# urllib.request — Extensible library for opening URLs, https://docs.python.org/3/library/urllib.request.html 
import urllib.request
# os — Miscellaneous operating system interfaces, https://docs.python.org/3/library/os.html
import os
# gzip — Support for gzip files, https://docs.python.org/3/library/gzip.html
import gzip
# sys — System-specific parameters and functions, https://docs.python.org/3/library/sys.html
import sys
# shutil — High-level file operations, https://docs.python.org/3/library/shutil.html
import shutil
# re — Regular expression operations, https://docs.python.org/3/library/re.html
import re
# lxml - XML and HTML with Python, https://lxml.de/
import lxml.html
# argparse — Parser for command-line options, arguments and subcommands, https://docs.python.org/3/library/argparse.html
from argparse import ArgumentParser

configuration = {
  'index': 'https://metadata.library.yale.edu/MARCXML/bib_20250706_full',
  'target_dir': 'raw-data/yale'
}

def download_file(file_name):
    """
    Downloads a file, saves it into a directory, uncompresses it and deletes the compressed version.
    The base URL and the target directory come from the configuration object.
    Parameters                              
    ----------
    file_name : str
        the name of the downloadable file
    """
    remote_file = configuration['index'] + '/' + file_name
    local_file = configuration['target_dir'] + '/' + file_name
    uncompressed_file = re.sub(r'.gz', '', local_file)
    print(f'downloading {remote_file} to {uncompressed_file} ...')

    if not os.path.exists(local_file) and not os.path.exists(uncompressed_file):
        try:
            urllib.request.urlretrieve(remote_file, local_file)

            with gzip.open(local_file, 'rb') as f_in:
                with open(uncompressed_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

        except urllib.error.HTTPError as e:
            print("A network problem occured: ", e)
    
    if os.path.exists(local_file):
        os.remove(local_file)

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--index", dest="index", help="the index page that contains list of files")
    parser.add_argument("-t", "--target_dir", dest="target_dir", help="the target directory where the files will be stored locally")
    args = parser.parse_args()

    if args.index is not None:
        configuration['index'] = args.index
    if args.target_dir is not None:
        configuration['target_dir'] = args.target_dir

    if not os.path.exists(configuration['target_dir']):
        os.makedirs(configuration['target_dir'])

    with urllib.request.urlopen(configuration['index']) as response:
        print(response)
        content = response.read()
        doc = lxml.html.fromstring(content)
        items = doc.findall('body/table/tr/td/a', {})
        for item in items:
            file_name = item.get('href')
            if re.search('\\.gz$', file_name):
                download_file(file_name)

if __name__ == '__main__':
    sys.exit(main())
