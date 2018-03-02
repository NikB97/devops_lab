#!/bin/bash

#installing python versions
pyenv install 2.7.14 && echo "python installed 2.7.14"
pyenv install 3.6.4  && echo "python installed 3.6.4"

#creating virtualenv
pyenv virtualenv 2.7.14 python2 && echo "virtualenv (python2) created"
pyenv virtualenv 3.6.4 python3  && echo "virtualenv (python3) created"


