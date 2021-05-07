sphinx-pcbdraw
==============

This is a basic Sphinx extension for creating board views from KiCAD ``.kicad_pcb`` files and embedding them into a Sphinx document. Utilizes PcbDraw_ created by yaqwsx. Requires KiCAD_ and KiKit_.

.. _PcbDraw: https://github.com/yaqwsx/PcbDraw
.. _KiCAD: https://www.kicad.org/
.. _KiKit: https://github.com/yaqwsx/KiKit

pcbdraw directive
+++++++++++++++++

Here are some examples.

.. code-block:: rst

   .. pcbdraw:: UPduino_v3.0.kicad_pcb

.. pcbdraw:: UPduino_v3.0.kicad_pcb

.. code-block:: rst

   .. pcbdraw:: UPduino_v3.0.kicad_pcb
      :back:
      :mirror:
      :placeholder:
      :no-drillholes:

.. pcbdraw:: UPduino_v3.0.kicad_pcb
   :back:
   :mirror:
   :placeholder:
   :no-drillholes:


.. code-block:: rst

   .. pcbdraw:: NINA-W102_minimal_breakout.kicad_pcb

.. pcbdraw:: NINA-W102_minimal_breakout.kicad_pcb


.. code-block:: rst

   .. pcbdraw:: ThisFileDoesntExist.kicad_pcb

.. pcbdraw:: ThisFileDoesntExist.kicad_pcb


options
-------

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
      :width:                              # width of the resulting image, defaults to 100%


pcb-components directive
++++++++++++++++++++++++

A list of all the components on a board can be created using this directive. It will default to only showing the components on the front side:

.. code-block:: rst

   .. pcb-components:: UPduino_v3.0.kicad_pcb
      
.. pcb-components:: UPduino_v3.0.kicad_pcb

Components from only the back side can be specified:

.. code-block:: rst

   .. pcb-components:: UPduino_v3.0.kicad_pcb
      :side: back
      
.. pcb-components:: UPduino_v3.0.kicad_pcb
   :side: back

Components from both sides can be specificed.:

.. code-block:: rst

   .. pcb-components:: NINA-W102_minimal_breakout.kicad_pcb
      :side: both
      
.. pcb-components:: NINA-W102_minimal_breakout.kicad_pcb
   :side: both

TODO
++++

pcbdraw global options

.. code-block:: python

    sphinx_pcbdraw_libs = ["lib/folder/one", "lib/folder/two"] # library folders to include for generation
    sphinx_pcbdraw_style = "path/to/style.json" # default style path or builtin
    sphinx_pcbdraw_remap = "path/to/remap.json" # default for remapping components
    sphinx_pcbdraw_hidden = ["component1", "component2"] # list of components to hide from all designs


License
+++++++

sphinx-pcbdraw is under the MIT license. Source code is avaiable at https://github.com/nobodywasishere/sphinx-pcbdraw.

Example kicad_pcb file `UPduino_v3.0.kicad_pcb` from https://github.com/tinyvision-ai-inc/UPduino-v3.0, Copyright tinyvision-ai-inc under the MIT License.

Example kicad_pcb file `NINA-W102_minimal_breakout.kicad_pcb` from https://github.com/rac2030/breakout-boards, Copyright Michel Racic under the MIT License.
