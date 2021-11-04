import pcbnew
import csv
import wx
import os
from wx.lib.scrolledpanel import ScrolledPanel
from functions import fun

class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "UI"
        self.category    = "Modify PCB"
        self.description = "Align the selected component to 0 degree"

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
       
    def Run(self):
        app   = wx.App()
        frame = wx.Frame(parent=None, title='Plugins', size=(200, 900))
        panel = ScrolledPanel(frame)
        panel.SetupScrolling()
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        
        button = []
        def addButton(label_name, function_name):
            button.append(wx.Button(panel, label = label_name, size=(190,50)))
            button[-1].Bind(wx.EVT_BUTTON, function_name)
            my_sizer.Add(button[-1], 0, wx.ALL | wx.CENTER, 5)
        
        addButton('PCB Refresh', fun.refresh)
        addButton('Align', fun.align)
        addButton('Align90', fun.align90)
        addButton('Pin report', fun.pin_report)
        addButton('Report', fun.report)

        panel.SetSizer(my_sizer)
        frame.Show()
        app.MainLoop()

Report().register()
