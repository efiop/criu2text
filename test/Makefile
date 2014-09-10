all: images_img test

images_img:
	mkdir $@
	setsid ./loop.sh < /dev/null &> /dev/null & \
	$(CRIU) dump -v4 -o dump.log -D $@ -t $${!} --shell-job

test: images_img
	mkdir -p images_text
	mkdir -p images_text_img
	bash test.sh

clean:
	rm -rf images_img images_text images_text_img
