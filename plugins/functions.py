import pcbnew
import wx
import csv
import os

class fun():
    def refresh(self):
        pcbnew.Refresh()

    def align(self):
        board = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(0)
        pcbnew.Refresh()

    def align90(self):
        board = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(0)
        pcbnew.Refresh()

    def pin_report(self):
        board       = pcbnew.GetBoard()
        csvfilename = 'pin_report.csv'
        csvfile     = open(csvfilename, 'w')
        csvwriter   = csv.writer(csvfile)
        csvwriter.writerow(["PIN REPORT"])
        csvwriter.writerow(["Reference", "Pin number", "X position", "Y Position", "Net Name"])
        for module in board.GetModules():
            report = []
            pads = module.Pads()
            for pad in pads:
                report = []
                report.append(module.GetReference())
                report.append(pad.GetName())
                report.append(pcbnew.ToMM(pad.GetPosition())[0])
                report.append(pcbnew.ToMM(pad.GetPosition())[1])
                report.append(pad.GetNetname())
                csvwriter.writerow(report)
        ans = os.path.dirname(os.path.realpath(__file__))
        wx.LogMessage("pin_report.csv is saved in " + ans)
        csvfile.close()

    def report(self):
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

