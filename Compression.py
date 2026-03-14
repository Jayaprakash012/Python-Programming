import zlib

str=b"this is a advance python class"

compress_data=zlib.compress(str)
decompress_data=zlib.decompress(compress_data)
print("compress_data",compress_data)
print("decompress_data",decompress_data)

