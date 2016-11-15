#!/bin/bash

if [ $TRAVIS_PULL_REQUEST == "true" ]; then
  echo "this is PR, exiting"
  exit 0
fi

# enable error reporting to the console
set -e 

# python generate.py

#clone `master' branch of the repository using encrypted GH_TOKEN for authentification
git clone https://${GH_TOKEN}@github.com/farhan687/appbaseio.github.io.git ../farhan687.github.io.master

# copy generated HTML site to `master' branch
cp -R ./index.html ./assets/* repo_images/* ../farhan687.github.io.master

# commit and push generated content to `master' branch
# since repository was cloned in write mode with token auth - we can push there
cd ../farhan687.github.io.master
git config user.email "farhan687@gmail.com"
git config user.name "Farhan Chauhan"
git add -A .
git commit -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --force https://${GH_TOKEN}@github.com/farhan687/appbaseio.github.io.git master