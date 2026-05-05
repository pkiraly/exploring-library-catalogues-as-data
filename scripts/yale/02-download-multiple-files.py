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

target_dir = 'raw-data/yale'

def download_file(base_url, file_name):
    print(f'downloading {file_name}...')
    remote_file = base_url + '/' + file_name
    local_file = target_dir + '/' + file_name
    uncompressed_file = re.sub(r'.gz', '', local_file)

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

def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("-i", "--index", dest="index", help="the index page that contains list of files")
    args = parser.parse_args()

    # default_url = 'https://metadata.library.yale.edu/MARCXML/bib_20250706_full'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if args.index is None:
        print(parser.print_help())
        exit()

    base_url = args.index

    with urllib.request.urlopen(base_url) as response:
        content = response.read()
        doc = lxml.html.fromstring(content)
        items = doc.findall('body/table/tr/td/a', {})
        for item in items:
            file_name = item.get('href')
            if re.search('\\.gz$', file_name):
                download_file(base_url, file_name)

if __name__ == '__main__':
    sys.exit(main())
