.PHONY: all test clean

PROTOBUF_DIR	= ../../protobuf
MAGIC_C_HEADER	= ../../include/magic.h
CRIU		= ../../criu

all: magic protobuf

test: protobuf magic
	make -C test CRIU=$(realpath $(CRIU))

magic: $(MAGIC_C_HEADER) protobuf
	python magic-gen.py $(MAGIC_C_HEADER)

protobuf:
	protoc -I=$(PROTOBUF_DIR) --python_out=./ $(PROTOBUF_DIR)/*.proto

clean:
	make -C test clean
	rm -rf *.pyc *_pb2.py __pycache__ magic.py
