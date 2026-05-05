import urllib.request
import os
import gzip
# shutil — High-level file operations, https://docs.python.org/3/library/shutil.html
import shutil
import re


url = 'https://metadata.library.yale.edu/MARCXML/bib_20250706_full/bib_20250706_full_000_00.xml.gz'
target_dir = 'raw-data/yale'
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

target_file = target_dir + '/bib_20250706_full_000_00.xml.gz'

urllib.request.urlretrieve(url, target_file)

with gzip.open(target_file, 'rb') as f_in:
    uncompressed_file = re.sub(r'.gz', '', target_file)
    with open(uncompressed_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove(target_file)
