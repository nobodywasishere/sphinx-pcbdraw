sphinx-pcbdraw
==============

This is a basic Sphinx extension for creating board views from KiCAD ``.kicad_pcb`` files and embedding them into a Sphinx document. Utilizes PcbDraw (https://github.com/yaqwsx/PcbDraw) created by yaqwsx.


An example that works::

   .. pcbdraw:: UPduino_v3.0.kicad_pcb

.. pcbdraw:: UPduino_v3.0.kicad_pcb

An example that doesn't work::

   # this file doesn't exist
   .. pcbdraw:: UPduin_v3.0.kicad_pcb

.. pcbdraw:: UPduin_v3.0.kicad_pcb

Example kicad_pcb file `UPduino_v3.0.kicad_pcb` from https://github.com/tinyvision-ai-inc/UPduino-v3.0, copyright tinyvision-ai-inc under the MIT License.
