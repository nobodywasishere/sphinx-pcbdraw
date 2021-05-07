import os, sys

sys.path.append(os.path.abspath("../sphinx_pcbdraw"))

extensions = ["sphinx-pcbdraw"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "env"]
