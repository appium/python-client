#!/bin/bash

EXIT_STATUS=0

if ! make lint ; then
  echo "Please run command 'make lint' on your local and commit the result"
  EXIT_STATUS=1
fi
if ! make format ; then
  echo "Please run command 'make format' on your local and commit the result"
  EXIT_STATUS=1
fi
if ! make unittest ARGS=--junitxml=./test/unit/junit.xml ; then
  EXIT_STATUS=1
fi

exit $EXIT_STATUS
