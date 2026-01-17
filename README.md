# VertexPad
The VertexPad is macropad with 8 keys, rotary encoder, OLED display and RGB lights for each key. I used KMK firmware for this macropad.
The idea is to use the pad for better workflow in any creative software. I designed it for Blender, but I plan to add more modes for other software.

## Overall Hackpad
- Case of 3 parts
- 8 keys
- EC11 rotary encoder
- 8 SK6812MINI LEDs - one for each key
- OLED Display
- With different Layers/Modes for different software, you can use the pad for many purposes.

<img src=assets/picture1.png alt="Hackpad Picture 1" width="300"/>
<img src=assets/picture2.png alt="Hackpad Picture 2" width="300"/>

## PCB
I made the PCB in KiCAD.

Schematic:

<img src=assets/schematic.png alt="Hackpad" width="500"/>

PCB: 

<img src=assets/pcb.png alt="Hackpad" width="500"/>

## CAD
I made the CAD in Autodesk Fusion which I already used a couple of times before. The hackpad's case is of three parts which fit together using M3 screws and heatset inserts.
We have a bottom, middle and top part. 

<img src=assets/cad.png alt="Hackpad" width="500"/>

## BOM
- 8x Cherry MX Switches
- 8x Blank DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x12mm SHCS Bolts
- 8x SK6812MINI LEDs
- 1x 0.91" 128x32 OLED Display
- XIAO RP2040
- 1x EC11 Rotary Encoder
- 1x case of 3 printed parts

## Future Updates
I plan to update the firmware to support more software. Next I plan to add Davinci Resolve.
