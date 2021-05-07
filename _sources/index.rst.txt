sphinx-pcbdraw
==============

This is a basic Sphinx extension for creating board views from KiCAD ``.kicad_pcb`` files and embedding them into a Sphinx document. Utilizes PcbDraw_ created by yaqwsx. Requires KiCAD_ and KiKit_.

.. _PcbDraw: https://github.com/yaqwsx/PcbDraw
.. _KiCAD: https://www.kicad.org/
.. _KiKit: https://github.com/yaqwsx/KiKit

Here are some examples.

.. code-block:: rst

   .. pcbdraw:: UPduino_v3.0.kicad_pcb

.. pcbdraw:: UPduino_v3.0.kicad_pcb

.. code-block:: rst

   .. pcbdraw:: UPduino_v3.0.kicad_pcb
      :back:
      :placeholder:
      :width: 75%

.. pcbdraw:: UPduino_v3.0.kicad_pcb
   :back:
   :placeholder:
   :width: 75%

.. code-block:: rst

   .. pcbdraw:: UPduino_v3.0.kicad_pcb
      :back:
      :mirror:
      :no-drillholes:

.. pcbdraw:: UPduino_v3.0.kicad_pcb
   :back:
   :mirror:
   :no-drillholes:

.. code-block:: rst

   .. pcbdraw:: ThisFileDoesntExist.kicad_pcb

.. pcbdraw:: ThisFileDoesntExist.kicad_pcb

Example kicad_pcb file `UPduino_v3.0.kicad_pcb` from https://github.com/tinyvision-ai-inc/UPduino-v3.0, Copyright tinyvision-ai-inc under the MIT License.

pcbdraw directive options
+++++++++++++++++++++++++

.. code-block:: rst

   .. pcbdraw:: path/to/pcb.kicad_pcb
      :style: path/to/style.json           # select a path/to/style.json
      # or selects a builtin style if not a proper path
      :placeholder:                        # place red squares in place of missing components
      :remap: path/to/remap.json           # use path/to/remap.json to remap components
      :no-drillholes:                      # don't make drillholes transparent
      :back:                               # draw the back of the board
      :mirror:                             # mirror board on x-axis
      :highlight: comma, separated, list   # highlight these components
      :filter: comma, separated, list      # only show these components
      :hidden: comma, separated, list      # don't show these components

TODO
++++

pcbdraw global options

.. code-block:: python

    sphinx_pcbdraw_libs = ["lib/folder/one", "lib/folder/two"] # library folders to include for generation
    sphinx_pcbdraw_style = "path/to/style.json" # default style path or builtin
    sphinx_pcbdraw_remap = "path/to/remap.json" # default for remapping components
    sphinx_pcbdraw_hidden = ["component1", "component2"] # list of components to hide from all designs
