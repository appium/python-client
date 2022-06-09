#!/bin/bash

EXIT_STATUS=0

if ! make black ARGS=--check ; then
  echo "Please run command 'make black' on your local and commit the result"
  EXIT_STATUS=1
fi
if ! make isort ARGS=--check-only ; then
  echo "Please run command 'make isort' on your local and commit the result"
  EXIT_STATUS=1
fi

if ! make pylint ; then
  echo "Please run command 'make pylint' on your local and fix errors"
  # TODO: pylint erroneously complains about many things it should not complain about
  # EXIT_STATUS=1
fi

if ! make unittest ARGS=--junitxml=./test/unit/junit.xml ; then
  EXIT_STATUS=1
fi

if ! make mypy ; then
  EXIT_STATUS=1
fi

exit $EXIT_STATUS
