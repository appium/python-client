#!/bin/bash

result=$(python -m autopep8 -r --global-config .config-pep8 -d .)
if [[ $result ]] ; then
  echo $result
  echo "Please run command 'python -m autopep8 -r --global-config .config-pep8 -i .' on your local and commit the result"
  exit 1
fi

result=$(python -m isort -rc . | grep -v "Skipped")
if [[ $result ]] ; then
  echo $result
  echo "Please run command 'python -m isort -rc .' on your local and commit the result"
  exit 1
fi

python -m pylint --rcfile .pylintrc appium test --errors-only
python -m pytest test/unit/
