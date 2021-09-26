# kicad

This repo will be used to create small functions in kicad pcbnew

## get_track_list(filename)
This function will list all the tracks in the given board.

It will return a list which contains 

<b>ans[0]</b> -> Track start and end point (x,y)

<b>ans[1]</b> -> Layer name in which track is present

<b>ans[2]</b> -> Netname of the track

<b>ans[3]</b> -> Track width in mm
