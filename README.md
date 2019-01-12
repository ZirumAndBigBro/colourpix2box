# colourpix2box
Python script to build in Aion on the basis of the existing game objects 

this file converst pixel (RGB) position from .bmp-file to npc coordinates ("colour".txt) for AION online game.
example result in result.txt
<spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
for integration in \AC-Game\data\static_data\spawns\(Npcs or gather)\New\location.xml file.

1. Modificate .bmp-file in paint.
2. Get information about RGB values from pixels, you used in .bmp-file. For that put each colour in palette located in upper left corner of your immage (starting in second row and second line). Run script in IDLE. This will show you RGB values from your palette.
3. Put game coordinates from your bottem left start point and adjust RGB values in colourpix2box.py and run it.
4. copy coordinates from "colour".txt and put it in \AC-Game\data\static_data\spawns\(Npcs or gather)\New\location.xml file.

Result see Example_colourpix2box.jpg
