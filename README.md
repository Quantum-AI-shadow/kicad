# kicad

This repo will be used to create small functions in kicad pcbnew

## get_track_list(filename)
This function will list all the tracks in the given board.
It will return a list which contains 
ans[0] -> Track start and end point (x,y)
ans[1] -> Layer name in which track is present
ans[2] -> Netname of the track
ans[3] -> Track width in mm
