#!/usr/bin/env bash

appium server --relaxed-security > appium_log.txt 2>&1 &
secondsStarted=$(date +%s)
while ! nc -z 127.0.0.1 4723; do
  sleep 0.1
  secondsElapsed=$(( $(date +%s) - secondsStarted ))
  if [[ $secondsElapsed -gt 30 ]]; then
    echo "Appium server was unable to start within 30 seconds timeout"
    exit 1
  fi
done
