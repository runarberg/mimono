pelican -s publishconf.py

heroku login

cd webpage
git add .
git commit -m "webpage update"
git push heroku master
