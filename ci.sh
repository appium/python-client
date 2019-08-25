#!/bin/bash

set -o pipefail

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
  LINT_RESULT=$(python -m pylint --rcfile .pylintrc appium test --errors-only 2>&1 | tee /dev/tty)
  if [[ $? -ne 0 ]] ; then
    EXIT_STATUS=1
  fi

  # FIXME: pylint x Python 3.7 cause this runtime error.
  # We must remove here when we drop Python 2 (and can update pylint) or
  # install newer pylint for Python 3.7 environment on CI
  if [[ $LINT_RESULT =~ "RuntimeError: generator raised StopIteration" ]] ; then
    EXIT_STATUS=0
  fi
)

(
  python -m pytest test/unit/
)
if [[ $? -ne 0 ]] ; then
  EXIT_STATUS=1
fi

exit $EXIT_STATUS
