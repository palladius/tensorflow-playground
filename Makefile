
# If you have an error:
# 1. Check that ~/tensorflow/ excists - if not, run make install-ubuntu or add for Mac and others
# 2. if you have the dir but doesn't find the libraries, try to trun the srouce/activate line.

validate-installation: hello

hello:
	source ~/tensorflow/bin/activate
	python 1-hello.py

getting-started:
	source ~/tensorflow/bin/activate
	python 2-getting-started.py


install-ubuntu:
	@echo "See https://www.tensorflow.org/install/install_linux#InstallingVirtualenv"
	sudo apt-get install python-pip python-dev python-virtualenv 
	virtualenv --system-site-packages  ~/tensorflow
	source ~/tensorflow/bin/activate
	pip install --upgrade tensorflow 
	echo "I should have installed TF on your ~/tensorflow dir with all libraries (py27 / CPU)"