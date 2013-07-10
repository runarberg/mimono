#! /usr/bin/env python

"""
A read-eval-print-loop to view the development version of the webpage
"""

import os
import subprocess
from subprocess import PIPE

subprocess.Popen(['pelican', '-s', 'devconf.py', '-r'],
                 stdin=PIPE, stdout=PIPE, stderr=PIPE)

os.chdir('webpage-dev')
subprocess.Popen(['python', '-m', 'SimpleHTTPServer'])

subprocess.call(['open', 'http://127.0.0.1:8000'])
