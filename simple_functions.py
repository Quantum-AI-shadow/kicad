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
        if(type(track) is pcbnew.TRACK):
            track_list.append(track)
            track_pos_list.append([ToMM(track.GetStart()), ToMM(track.GetEnd())])
            track_layer_list.append(track.GetLayerName())
            track_net_list.append(track.GetNetname())
            track_width_list.append(track.GetWidth()/1e6) # Converting to mm
    return [track_pos_list, track_layer_list, track_net_list, track_width_list]   # change the return to whatever you want

def get_via_list(filename):
    via_list       = []
    via_drill_list = []
    via_width_list = []
    via_net_list   = []
    board = pcbnew.LoadBoard(filename)
    tracks = board.GetTracks()
    for via in tracks:
        if(type(via) is pcbnew.VIA):
            via_list.append(via)
            via_width_list.append(via.GetWidth()/1e6)
            via_drill_list.append(via.GetDrill()/1e6)
            via_net_list.append(via.GetNetname())
    return [via_width_list, via_drill_list, via_net_list]

ans = get_track_list("/home/quantum/Desktop/kicad/arduno_mini/arduno_mini.kicad_pcb")
for i in ans:
    print(i)
    print()
ans = get_via_list("/home/quantum/Desktop/kicad/arduno_mini/arduno_mini.kicad_pcb")
for i in ans:
    print(i)
    print()
