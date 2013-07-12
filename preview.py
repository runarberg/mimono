#! /usr/bin/env python

"""
A read-eval-print-loop to view the development version of the webpage
"""

import os
import subprocess

from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from subprocess import PIPE

def run_server():
    port = 8000
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print "serving at port ", port
    httpd.serve_forever()

    
if __name__ in "__main__":
    subprocess.Popen(['pelican', '-s', 'devconf.py', '-r'],
                     stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # TODO: Have to make replace the 'open' command with a UNIX neutral command
    subprocess.call(['open', 'http://127.0.0.1:8000'])

    os.chdir('webpage-dev')
    run_server()

