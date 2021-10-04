from pcbnew import *
import pcbnew

def get_via_list(filename):
    viaCount = 0
    board = pcbnew.LoadBoard(filename)
    tracks = board.GetTracks()
    for via in tracks:
        if(type(via) is pcbnew.VIA):
            viaCount += 1
            print("Via:", viaCount)
            print("Width:", via.GetWidth()/1e6)
            print("Drill:",via.GetDrill()/1e6)
            print("Netname:",via.GetNetname())
            print("Position:", ToMM(via.GetPosition()))
            print()


ans = get_via_list("/home/quantum/Desktop/kicad/arduno_mini/arduno_mini.kicad_pcb")
