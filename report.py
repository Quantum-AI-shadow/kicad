import pcbnew
import csv

#board      = pcbnew.GetBoard()
filename    = '/home/quantum/Desktop/kicad/arduno_mini/arduno_mini/arduno_mini.kicad_pcb'
board       = pcbnew.LoadBoard(filename)
csvfilename = 'report.csv'
csvfile     = open(csvfilename, 'w')
csvwriter   = csv.writer(csvfile)

print("########## TRACKS: ##########")
csvwriter.writerow(["TRACK LIST"])
csvwriter.writerow(["Width", "Start Point", "End Point", "Layer Name", "Net Name"])
for track in board.GetTracks():
    if(type(track) == pcbnew.TRACK):
        print('Width   : ',track.GetWidth()/1e6)
        print('(x1, y1): ',pcbnew.ToMM(track.GetStart()))
        print('(x2, y2): ',pcbnew.ToMM(track.GetEnd()))
        print('Layer   : ',track.GetLayerName())
        print('Net Name: ',track.GetNetname())
        print()
        csvwriter.writerow([track.GetWidth()/1e6, pcbnew.ToMM(track.GetStart()), pcbnew.ToMM(track.GetEnd()), track.GetLayerName(), track.GetNetname()])

print("########## VIA LIST: ##########")
csvwriter.writerow([])
csvwriter.writerow(["VIA LIST"])
csvwriter.writerow(["Width", "Drill", "Position", "Net Name"])
for via in board.GetTracks():
    if(type(via) == pcbnew.VIA):
        print('Width   : ',via.GetWidth()/1e6)
        print('Drill   : ',via.GetDrill()/1e6)
        print('Position: ',pcbnew.ToMM(via.GetPosition()))
        print('Net Name: ',via.GetNetname())
        print()
        csvwriter.writerow([via.GetWidth()/1e6, via.GetDrill()/1e6, pcbnew.ToMM(via.GetPosition()), via.GetNetname()])

print("########## COMPONENT LIST: ##########")
csvwriter.writerow([])
csvwriter.writerow(["COMP LIST"])
csvwriter.writerow(["Reference", "Position", "Value", "Flipped", "Angle"])
for comp in board.GetModules():
    print('Reference: ',comp.GetReference())
    print('Position : ',pcbnew.ToMM(comp.GetPosition()))
    print('Value    : ',comp.GetValue())
    print('Flipped  : ',comp.IsFlipped())
    print('Angle    : ',comp.GetOrientation()/10)
    print()
    csvwriter.writerow([comp.GetReference(), pcbnew.ToMM(comp.GetPosition()), comp.GetValue(), comp.IsFlipped(), comp.GetOrientation()/10])

csvfile.close()
