from pcbnew import *
import pcbnew

def get_track_list(filename):
    track_list       = []
    track_pos_list   = []
    track_width_list = []
    track_layer_list = []
    track_net_list   = []
    board = pcbnew.LoadBoard(filename)
    tracks = board.GetTracks()
    for track in tracks:
        if(type(track) is not pcbnew.VIA):
            track_list.append(track)
            track_pos_list.append([ToMM(track.GetStart()), ToMM(track.GetEnd())])
            track_layer_list.append(track.GetLayerName())
            track_net_list.append(track.GetNetname())
            track_width_list.append(track.GetWidth()/1e6) # Converting to mm
    return track   # change the return to whatever you want


ans = get_track_list("/home/quantum/Desktop/kicad/arduno_mini/arduno_mini.kicad_pcb")
for i in ans:
    print(i)
