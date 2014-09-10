images_list=$(cd images_img; ls -1 *.img | sed -e 's/\..*$//')

function _exit {
	if [ $? -ne 0 ]; then
		echo "FAIL"
		exit -1
	fi
}

for x in $images_list
do
	echo "===  $x"
	if [[ $x == pages* ]]; then
		echo "skip"
		continue
	fi

	echo " -- to text"
	python ../criu2text.py to-text images_img/"$x"".img" images_text/ || _exit $?
	echo " -- to img"
	python ../criu2text.py to-img images_text/"$x" images_text_img/ || _exit $?
	echo " -- cmp"
	cmp images_img/"$x"".img" images_text_img/"$x"".img" || _exit $?
	echo "=== done"
done
