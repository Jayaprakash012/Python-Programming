import zlib

str=b"this is a advance python class"

compress_data=zlib.compress(str)
decompress_data=zlib.decompress(compress_data)
print("compress_data",compress_data)
print("decompress_data",decompress_data)

import gzip
with gzip.open('file.txt.gz', 'wt') as f:
    f.write('This is a test file.')
    f.close()
with gzip.open('file.txt.gz', 'rt') as f:
    print(f.read())
    f.close()    
#COMPRESSING BETWEEN zlib and gzip
import zipfile
with zipfile.ZipFile('file.zip', 'w') as zip_file:
    zip_file.write('file.txt.gz')
 # new file
with zipfile.ZipFile('file.zip', 'r') as zip_file:
    zip_file.write('compressed_file.txt.gz')
with zipfile.ZipFile('file.zip', 'r') as zip_file:
     print(zip_file.namelist())   