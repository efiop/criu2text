#!/bin/python
import os, sys
import struct
import google
import shutil

import images

def img2text(fin):
    # Read magic cookie to identify criu image
    buf = fin.read(4)

    # Convert cookie into "0x12345.." string to
    # use it as a key in criu.magic dict
    cookie, = struct.unpack('i', buf)
    cookie = "0x{0:x}".format(cookie)

    # Write cookie into file named magic
    fout = open("magic", 'w+')
    fout.write(cookie)
    fout.close()

    if cookie in images.pb.keys():
    	pb = images.pb[cookie]()
        num = 0

    	while True:
            # Read size of the following pb message
            buf = fin.read(4)
            if buf == '':
                break

            size, = struct.unpack('i', buf)

            # Read pb message
            pb.ParseFromString(fin.read(size))

            # Write text representation of
            # pb message into num file
            fout = open(str(num), 'w+')
            google.protobuf.text_format.PrintMessage(pb, fout)
            fout.close()

            num += 1
            # pagemap.img is a special one. It starts with
            # pagemap_head message and is followed by an
            # array of pagemap_entry's.
            if cookie == images.PAGEMAP_MAGIC:
                pb = images.pagemap_entry()

    else:
	    print("not criu image or unknown format")
            exit(1)

def text2img(fout):
    # Open magic file to get magic cookie
    fin = open("magic", 'r')
    cookie = fin.read()
    fin.close()

    if cookie in images.pb.keys():
        # Write magic cookie into img file
        fout.write(struct.pack('i', int(cookie,16)))

        # Corresponding function that we need to call
        # to init pb message
        pb_init_function = images.pb[cookie]

        num = 0
        while True:
            if not os.path.isfile(str(num)):
                break

            pb = pb_init_function()

            # Read pb message int text format from
            # file num
            fin = open(str(num), 'r')
            pb_text = fin.read()
            fin.close()

            # Parse pb from text format and write
            # it to img file
            google.protobuf.text_format.Merge(pb_text, pb)
            size = len(pb.SerializeToString())
            fout.write(struct.pack('i', size))
            fout.write(pb.SerializeToString())

            num += 1
            # pagemap.img is a special one. It starts with
            # pagemap_head message and is followed by an
            # array of pagemap_entry's.
            if cookie == images.PAGEMAP_MAGIC:
                pb_init_function = images.pagemap_entry

    else:
        print("unknown format")
        exit(1)

def main(argv):
	usage = "Usage: criu2text to-text IMG_IN [WORK_DIR]\n"\
                "or:    criu2text to-img TEXT_DIR_IN [WORK_DIR]\n"\
                "\n"\
                "Examples:\n"\
                "1) $ criu2text to-text core-1234.img text_imgs_dir\n"\
                "   $ ls text_imgs_dir\n"\
                "   core-1234\n"\
                "2) $ criu2text to-img text_imgs_dir/core-1234 imgs_dir\n"\
                "   $ ls imgs_dir\n"\
                "   core-1234.img\n"

	if len(argv) > 4 or len(argv) < 3:
		print(usage)
		exit(1)

        if len(argv) == 4:
                work_dir = argv[3] + '/'
        else:
                work_dir = "./"

        if argv[1] == "to-text":
            img_file = os.path.abspath(argv[2])

            text_dir = work_dir + os.path.splitext(os.path.basename(argv[2]))[0]
            text_dir = os.path.abspath(text_dir)

            if os.path.exists(text_dir):
                shutil.rmtree(text_dir)
            os.mkdir(text_dir)
            os.chdir(text_dir)

            with open(img_file, 'r') as fin:
                img2text(fin)

        elif argv[1] == "to-img":
            img_file = work_dir + os.path.basename(argv[2]) + ".img"
            img_file = os.path.abspath(img_file)

            text_dir = argv[2]

            os.chdir(text_dir)

            with open(img_file, 'w+') as fout:
                text2img(fout)

        else:
            print(usage)
            exit(1)

if __name__ == "__main__":
	main(sys.argv)
