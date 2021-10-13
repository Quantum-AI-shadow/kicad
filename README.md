# kicad

This repo will be used to create small functions in kicad pcbnew

## create.py:

This contains definitions for creating via, track and zones.

## getViaList.py

This contains function to list all the via present in the board.

## report.py

This will create a report in csv file which includes track, via and components.

Change the file name and run it in python3

<b> Track: </b>

Width, Start point, End point, Layer name, Net name

<b> Via: </b>

Width, Drill, Position, Net name

<b> Component: </b>

Reference, Position, Value, Flipped, Angle

## report_tk.py

This is same as report, but there is a file dialog to choose pcb board file.

## simple_functions.py

This is to collect some usefule functions in kicad scripting.

# Plugins

To use these plugins, save the .py file in /usr/share/kicad/scripting/plugins/

Refresh external plugins in kicad pcbnew

## report

This plugin will generate the report which will contain track, via and component details

## align

This will align the selected component to 90 degree 

## Pin report

This will generate a csv file with pin reference ID, Pin name, X and Y position with netname.

# Tutorial:
https://crypticquantum.wordpress.com/

