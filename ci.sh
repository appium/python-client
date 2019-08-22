#!/bin/bash

EXIT_STATUS=0
if ! python -m autopep8 --exit-code -a -r --global-config .config-pep8 -i . ; then
  echo "Please run command 'python -m autopep8 -a -r --global-config .config-pep8 -i .' on your local and commit the result"
  EXIT_STATUS=1
fi

if ! python -m isort --check-only -rc . ; then
  echo "Please run command 'python -m isort -rc .' on your local and commit the result"
  EXIT_STATUS=1
fi

(
  python -m pylint --rcfile .pylintrc appium test --errors-only
)
if [ $? -eq 1 ] ; then
  EXIT_STATUS=1
fi

(
  python -m pytest test/unit/
)
if [ $? -eq 1 ] ; then
  EXIT_STATUS=1
fi

exit $EXIT_STATUS