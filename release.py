# TODO: convert below commands into python
# set -e

# declare newversion
# declare current_version
# declare sure

# current_version="$(grep -E version ./appium/version.py | sed 's,version *= *.\(\([0-9]*[.]*\)\{3\,4\}\).,\1,g')"
# echo -en "The current version is \033[1;33m$current_version\033[0m, type a new one\n"
# echo -en "\033[1;32mnew version:\033[0m \n"
# read -r newversion

# ######
# function update_files () {
#     sed -i.back -e "s,$current_version,$newversion,g" appium/version.py
# }

# function commit_version_code () {
#     if [ $DRY_RUN ]; then
#         echo -en "\033[1;31m[DRY_RUN]\033[0m call 'git commit ./appium/version.py -m \"Bump $newversion\"'\n"
#     else
#         git commit ./appium/version.py -m "Bump $newversion"
#     fi
# }

# function tag_and_generate_changelog () {
#     if [ $DRY_RUN ]; then
#         echo -en "\033[1;31m[DRY_RUN]\033[0m call 'git tag \"v${newversion}\"', generate CHANGELOG.rst and" \
#                  "'git commit CHANGELOG.rst -m \"Update changelog for $newversion\"'\n"
#     else
#         git tag "v${newversion}"
#         gitchangelog > CHANGELOG.rst
#         git commit CHANGELOG.rst -m "Update changelog for $newversion"
#     fi
# }

# function upload_sdist () {
#     if [ $DRY_RUN ]; then
#         echo -en "\033[1;31m[DRY_RUN]\033[0m call 'twine upload \"dist/Appium-Python-Client-$newversion.tar.gz\"'\n"
#     else
#         twine upload "dist/Appium-Python-Client-$newversion.tar.gz"
#     fi
# }

# function push_changes_to_master () {
#     echo "Push changes and the tag to the master"
#     if [ $DRY_RUN ]; then
#         echo -en "\033[1;31m[DRY_RUN]\033[0m call 'git push origin master' and git 'push origin \"v$newversion\"'\n"
#     else
#         git push origin master
#         git push origin "v$newversion"
#     fi
# }
# ######

# echo -en "\033[A\033[A\rI will make a new commit named \033[1;33m'Bump $newversion'\033[0m\n"
# echo -en "Are you sure? [\033[1;32myes\033[0m or \033[1;31mno\033[0m]\n"
# read -r sure

# if [ "${sure}" == "yes" ]; then
#     update_files
#     echo -en "New release: \033[1;32m$newversion\033[0m\n"
#     commit_version_code
#     python setup.py sdist # build a release tar file in /dist

#     tag_and_generate_changelog

#     echo "Publish the built module"
#     upload_sdist
#     push_changes_to_master
# fi

def main():
    print("do main method")

if __name__ == '__main__':
    main()
