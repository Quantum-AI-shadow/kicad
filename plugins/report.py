import pcbnew
import csv
import wx
import os

class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "Report"
        self.category    = "Modify PCB"
        self.description = "Create a csv file with track, via and component report"
        
    def Run(self):
        board       = pcbnew.GetBoard()
        csvfilename = 'report.csv'
        csvfile     = open(csvfilename, 'w')
        csvwriter   = csv.writer(csvfile)
        
        csvwriter.writerow(["TRACK LIST"])
        csvwriter.writerow(["Width", "Start Point", "End Point", "Layer Name", "Net Name"])
        for track in board.GetTracks():
            if(type(track) == pcbnew.TRACK):
                csvwriter.writerow([track.GetWidth()/1e6, pcbnew.ToMM(track.GetStart()), pcbnew.ToMM(track.GetEnd()), track.GetLayerName(), track.GetNetname()])
        
        csvwriter.writerow([])
        csvwriter.writerow(["VIA LIST"])
        csvwriter.writerow(["Type", "Width", "Drill", "Position", "Net Name"])
        for via in board.GetTracks():
            if(type(via) == pcbnew.VIA):
                csvwriter.writerow(["THROUGH", via.GetWidth()/1e6, via.GetDrill()/1e6, pcbnew.ToMM(via.GetPosition()), via.GetNetname()])
        
        csvwriter.writerow([])
        csvwriter.writerow(["COMP LIST"])
        csvwriter.writerow(["Reference", "Position", "Value", "Flipped", "Angle"])
        for comp in board.GetModules():
            csvwriter.writerow([comp.GetReference(), pcbnew.ToMM(comp.GetPosition()), comp.GetValue(), comp.IsFlipped(), comp.GetOrientation()/10])
        ans = os.path.dirname(os.path.realpath(__file__))
        wx.LogMessage("report.csv is saved in " + ans)
        csvfile.close()
Report().register()
