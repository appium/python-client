#!/bin/bash

declare newversion
declare current_version
declare sure

current_version="$(grep -E version ./appium/version.py | sed 's,version *= *.\(\([0-9]*[.]*\)\{3\,4\}\).,\1,g')"
echo -en "The current version is \033[1;33m$current_version\033[0m, type a new one\n"
echo -en "\033[1;32mnew version:\033[0m \n"
read -r newversion

function update_files (){
    sed -i.back -e "s,$current_version,$newversion,g" appium/version.py
}

echo -en "\033[A\033[A\rI will make a new commit named \033[1;33m'New release $newversion'\033[0m\n"
echo -en "Are you sure? [\033[1;32myes\033[0m or \033[1;31mno\033[0m]\n"
read -r sure

if [ "${sure}" == "yes" ]; then
    update_files
    echo -en "New release: \033[1;32m$newversion\033[0m\n"
    git commit ./appium/version.py -m "Bump $newversion"
    python setup.py sdist # build a release tar file in /dist

    git tag "v${newversion}"

    gitchangelog > CHANGELOG.rst
    git commit CHANGELOG.rst -m "Update changelog for $newversion"

    echo "Publish the built module"
    twine upload "dist/Appium-Python-Client-$newversion.tar.gz"

    echo "Push changes and the tag to the master"
    git push origin master
    git push origin "v${newversion}"
fi;
