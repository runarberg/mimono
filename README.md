MIMONO
======

Chantal Uto's kids clothing line

Directories
-----------

* `articles/` Individual articles related to the project, written in [Markdown](http://daringfireball.net/projects/markdown)
* `pictures/` Design photographs
* `theme/`    Jinja2 template files for [Pelican-generated](http://getpelican.com) web files
* `webpage/`  The public webpage files for the project

Make the webpage
----------------

The webpage requires `Pelican` and the `Markdown` packages for Python `pip install pelican markdown`.

Then simply run `pelican -s devconf.py` for development version of the webpage or `pelican -s publishconf.py` for the public version.

### Write new articles

You need to create a new markdown file for each new article you write, `article.md` for example.

### Deploy to Heroku

The webpage is now hosted on Heroku. To deploy there simply run the `publish.command` shell script. You can also preview on your on your local server by running `preview.command` and visiting <http://127.0.0.1:8000> in your browser.