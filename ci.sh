#!/bin/bash

result=$(python -m autopep8 -r --global-config .config-pep8 -d .)
if [[ $result ]] ; then
  echo $result
  echo "Please run command 'python -m autopep8 -r --global-config .config-pep8 -i .' on your local and commit the result"
  exit 1
fi

python -m pylint --rcfile .pylintrc appium test --py3k
python -m pytest test/unit/*
