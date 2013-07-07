MIMONO
======

Chantal Uto's kids clothing line

directories
-----------

* `articles/` Individual articles related to the project, written in [Markdown](http://daringfireball.net/projects/markdown)
* `pictures/` Design photographs
* `theme/`    Jinja2 template files for [Pelican-generated](http://getpelican.com) web files
* `webpage/`  The public webpage files for the project

Make the webpage
----------------

The webpage requires `Pelican` and the `Markdown` packages for Python `pip install pelican markdown`.

Then simply run `pelican -s devconf.py` for development version of the webpage or `pelican -s publishconf.py` for the public version.