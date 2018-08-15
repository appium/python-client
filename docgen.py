#!/usr/bin/env python

# PyPi expects a reStructuredText (http://docutils.sourceforge.net/rst.html)
# document for its readme. This takes the Github one and makes the requisite
# file. Run when README.md is changed and those changes should be reflected
# on PyPi.

import pandoc
import os

pandoc.core.PANDOC_PATH = os.environ['PANDOC_HOME']

doc = pandoc.Document()
doc.markdown = open('README.md').read()
f = open('README.txt', 'w+')
f.write(doc.rst)
f.close()
