from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util import logging

import os, sys, subprocess, re

logger = logging.getLogger(__name__)

class pcb_components(nodes.General, nodes.Inline, nodes.Element):
    '''Base class for pcb_components node'''
    pass

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
    
    # global_variable_options = {
    #     "sphinx_pcbdraw_output_format": ["svg", "png"],
    #     "sphinx_pcbdraw_libs": ["default"],
    #     "sphinx_pcbdraw_style": ["default"],
    #     "sphinx_pcbdraw_remap": ["default"]
    # }

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
            logger.info("File exists: {}".format(pcb_file))
        else:
            logger.error("File does not exist: {}".format(pcb_file))
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

        # I know this isn't the correct way to do this, and that I should break this out
        # into a node + node visitor instead
        full_path = os.path.abspath("_build/pcbdraw/")
        outfile = os.path.join(full_path, pcb_file + outfileopt + ".svg")

        cmd = "pcbdraw {infile} {outfile} {options}".format(
            options=options,
            infile=pcb_file,
            outfile=outfile
        )
        print("Running cmd:", cmd)
        subprocess.run(cmd, shell=True)

        image_node = nodes.image()
        # for some reason it likes to remove the leading forward slash
        image_node['uri'] = "/" + outfile
        image_node['width'] = self.options['width'] if 'width' in self.options else '100%'

        return [image_node]

class PCBComponents(Directive):
    has_content = True

    option_spec = {
        'side': str,
    }

    comps = ""

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
            logger.info("File exists: {}".format(pcb_file))
        else:
            logger.error("File does not exist: {}".format(pcb_file))
            return [nodes.error(
                None,
                nodes.paragraph(text=("sphinx-pcbdraw: "
                    "File does not exist: " + pcb_file)),
            )]

        if 'side' in self.options:
            if self.options['side'] == 'front':
                comps = str(subprocess.check_output("pcbdraw {infile} out.svg --list-components".format(infile=pcb_file), shell=True))
            elif self.options['side'] == 'back':
                comps = str(subprocess.check_output("pcbdraw {infile} out.svg --list-components --back".format(infile=pcb_file), shell=True))
            elif self.options['side'] == 'both':
                comps  = str(subprocess.check_output("pcbdraw {infile} out.svg --list-components".format(infile=pcb_file), shell=True))
                comps += str(subprocess.check_output("pcbdraw {infile} out.svg --list-components --back".format(infile=pcb_file), shell=True))
            else:
                raise Exception("Unknown option for :side:: {}".format(self.options['side']))
        else:
            comps = str(subprocess.check_output("pcbdraw {infile} out.svg --list-components".format(infile=pcb_file), shell=True))
            
        # comps = re.sub(" at .* package ", "", comps)
        comps = comps.split('\\n')
        for i in range(len(comps)):
            comps[i] = re.sub('^.* package ', '', comps[i])
            comps[i] = re.sub(' at \[.*', '', comps[i])
            if ":" not in comps[i]:
                comps[i] = ""
        comps = list(set(comps))
        comps.sort()

        comps = ['Library:Component'] + comps

        node = pcb_components()
        node['comps'] = comps
        node['side'] = self.options['side'] if 'side' in self.options else ''
        self.add_name(node)
        return [node]

def visit_pcb_components_node(self, node):
    table_str = "<table class='docutils'>"
    for t in range(len(node['comps'])):
        if ":" not in node['comps'][t]:
            pass
        else:
            table_str += "<tr>"
            for q in node['comps'][t].split(":"):
                if t == 0:
                    table_str += "<th>{}</th>".format(q)
                else:
                    table_str += "<td>{}</td>".format(q)
            table_str += "</tr>"
            
    table_str += "</table>"
    self.body.append(table_str)

def depart_pcb_components_node(self, node):
    pass

def setup(app):
    app.add_node(pcb_components,
        html=(visit_pcb_components_node, depart_pcb_components_node))
    app.add_directive("pcbdraw", PCBDraw)
    app.add_directive("pcb-components", PCBComponents)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
