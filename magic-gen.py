import os, sys
import struct

# This program parses criu magic.h file and produces
# magic.py with all *_MAGIC constants except RAW and V1.
def main(argv):
    if len(argv) != 2:
        print("Usage: magic-gen.py path/to/image.h")
        exit(1)

    magic_c_header = argv[1]
    magic_py = "magic.py"

    out = open(magic_py, 'w+')

    magic = {}

    f = open(magic_c_header, 'r')
    for line in f:
    	split = line.split()

    	if len(split) < 3:
            continue

	if not '#define' in split[0]:
	    continue

	key = split[1]
	value = split[2]

	if value in magic:
            value = magic[value]

	magic[key] = value

        if value == '0x0' or value == '1':
            continue

        out.write(key+" = "+"\'"+value+"\'\n")

    out.close()

if __name__ == "__main__":
    main(sys.argv)
