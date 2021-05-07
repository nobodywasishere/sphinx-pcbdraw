import os, sys
from datetime import datetime

sys.path.append(os.path.abspath("../sphinx_pcbdraw"))

extensions = ["sphinx-pcbdraw"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "env"]

project = 'sphinx-pcbdraw'
year = datetime.now().year
copyright = u"%d Michael Riegert" % year

html_theme_options = {
    'description': 'a basic Sphinx extension for creating board views from KiCAD files',
    "fixed_sidebar": True,
}