#! /bin/bash
sudo pip install virtualenv virtualenvwrapper
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
mkvirtualenv intrinsic -p python3
workon intrinsic
sudo apt-get install -y libeigen3-dev
pip install Pillow Cython numpy scipy scikit-image scikit-learn snakeviz numba
cd krahenbuhl2013
make
cd ..
python3 $1 $2
deactivate

