import pcbnew
import csv
import wx
import os

class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "Align"
        self.category    = "Modify PCB"
        self.description = "Align the selected component to 0 degree"
        self.show_toolbar_button = True
        
    def Run(self):
        board       = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(900)
        pcbnew.Refresh()
Report().register()
