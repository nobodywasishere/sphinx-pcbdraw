from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util import logging

import os, sys, subprocess

logger = logging.getLogger(__name__)

class PCBDraw(Directive):
    has_content = True

    # required_arguments = 1
    # optional_arguments = 8

    # final_argument_whitespace = False
    #
    option_spec = {
        'style': str,
        'placeholder': bool,
        'remap': str,
        'no-drillholes': bool,
        'back': bool,
        'mirror': bool,
        'highlight': str,
        'filter': str,
        'width': str
    }
    def run(self):
        try:
            import pcbnew
        except Exception as e:
            logger.error(e)
            return [nodes.error(
                None,
                nodes.paragraph(text=("sphinx-pcbdraw: "
                    + str(e))),
            )]

        pcb_file = self.content[0]
        if os.path.exists(pcb_file):
            logger.info("File exists")
        else:
            logger.error("File does not exist")
            return [nodes.error(
                None,
                nodes.paragraph(text=("sphinx-pcbdraw: "
                    "File does not exist: " + pcb_file)),
            )]

        options = ""
        outfileopt = ""

        if 'style' in self.options:
            options += " --style '{}'".format(self.options['style'])
            outfileopt += "_style"

        if 'placeholder' in self.options:
            options += " --placeholder"
            outfileopt += "_placeholder"

        if 'remap' in self.options:
            options += " --remap '{}'".format(self.options['remap'])
            outfileopt += "_remap"

        if 'no-drillholes' in self.options:
            options += " --no-drillholes"
            outfileopt += "_no-drillholes"

        if 'back' in self.options:
            options += " --back"
            outfileopt += "_back"

        if 'mirror' in self.options:
            options += " --mirror"
            outfileopt += "_mirror"

        if 'highlight' in self.options:
            options += " --highlight '{}'".format(self.options['highlight'])
            outfileopt += "_highlight"

        if 'filter' in self.options:
            options += " --filter '{}'".format(self.options['filter'])
            outfileopt += "_filter"

        subprocess.run("mkdir -p _build/pcbdraw/", shell=True)

        outfile = "_build/pcbdraw/" + pcb_file + outfileopt + ".svg"

        cmd = "pcbdraw {infile} {outfile} {options}".format(
            options=options,
            infile=pcb_file,
            outfile=outfile
        )
        print("Running cmd:", cmd)
        subprocess.run(cmd, shell=True)

        image_node = nodes.image()
        image_node['uri'] = outfile
        image_node['width'] = self.options['width'] if 'width' in self.options else '100%'

        return [image_node]

        return [paragraph_node]

def setup(app):
    app.add_directive("pcbdraw", PCBDraw)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
