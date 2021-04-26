from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util import logging

import os, sys, subprocess

logger = logging.getLogger(__name__)

class PCBDraw(Directive):
    has_content = True

    def run(self):
        pcb_file = self.content[0]
        if os.path.exists(pcb_file):
            logger.info("File exists")
        else:
            logger.error("File does not exist")
            return [nodes.error(
                None,
                nodes.paragraph(text="File does not exist:"),
                nodes.paragraph(text=pcb_file)
            )]
        options = ""
        outfile = pcb_file + ".svg"
        cmd = "pcbdraw {options} {infile} {outfile}".format(
            options=options,
            infile=pcb_file,
            outfile=outfile
        )
        subprocess.run(cmd, shell=True)
        par = "<img src='{src}'/>".format(src=outfile)
        paragraph_node = nodes.image()
        paragraph_node['uri'] = outfile
        return [paragraph_node]

def setup(app):
    app.add_directive("pcbdraw", PCBDraw)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
