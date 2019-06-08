#!/usr/bin/env bash

# This script was copy-pasted from https://docs.microsoft.com/en-us/azure/devops/pipelines/languages/android?view=azure-devops#test-on-the-android-emulator
# with some changes

# Install AVD files
declare -r emulator="system-images;android-${ANDROID_SDK_VERSION};google_apis;x86"
echo "y" | ${ANDROID_HOME}/tools/bin/sdkmanager --install "$emulator"

# Show a list of emulators
${ANDROID_HOME}/tools/bin/avdmanager list

# Create emulator
echo "no" | ${ANDROID_HOME}/tools/bin/avdmanager create avd -d "Nexus 5X" -n testemulator -k "${emulator}" --force

echo ${ANDROID_HOME}/emulator/emulator -list-avds

echo "Starting emulator"

# Start emulator in background
nohup ${ANDROID_HOME}/emulator/emulator -avd testemulator -no-boot-anim -no-snapshot > /dev/null 2>&1 &
${ANDROID_HOME}/platform-tools/adb wait-for-device shell 'while [[ -z $(getprop sys.boot_completed | tr -d '\r') ]]; do sleep 1; done; input keyevent 82'

${ANDROID_HOME}/platform-tools/adb devices

echo "Emulator started"
