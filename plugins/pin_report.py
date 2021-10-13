import pcbnew
import csv
import wx
import os

class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "Pin Report"
        self.category    = "Modify PCB"
        self.description = "Create a csv file with track, via and component report"
        
    def Run(self):
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
Report().register()
