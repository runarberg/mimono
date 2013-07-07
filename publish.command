#!/bin/sh
cd "`dirname "$0"`"

heroku login

pelican -s publishconf.py

cd webpage/
git add .
git commit -m "webpage update"
git push heroku master
