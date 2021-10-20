import pcbnew
import csv
import wx
import os


class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "Shortcut"
        self.category    = "Modify PCB"
        self.description = "Align the selected component to 0 degree"
        
    def Align(self):
        board       = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(0)
        pcbnew.Refresh()
        addMenu()

    def Align90(self):
        board = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(900)
        pcbnew.Refresh()
        addMenu()
    
    def Run(self):
        addMenu()

def addMenu():
    windows    = wx.GetTopLevelWindows()
    pcbwindow  = list(filter(lambda w: 1, windows))
    menuBar = pcbwindow[2].MenuBar
    
    def add_fun(funName, shortcut, name):
        my_id = wx.NewId()
        entry = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord(shortcut), my_id)
        menuBar.Bind(wx.EVT_MENU, funName, id=my_id)
        toolsMenu = menuBar.GetMenu(menuBar.FindMenu("Tools"))
        tools = toolsMenu.Append(my_id, name)
        tools.SetAccel(entry)
    
    add_fun(Report.Align, '1', 'Align')    
    add_fun(Report.Align90, '2', 'Align90')    

    #my_id = wx.NewId()
    #entry = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('1'), my_id)
    #menuBar.Bind(wx.EVT_MENU, Report.Align, id=my_id)
    #toolsMenu = menuBar.GetMenu(menuBar.FindMenu("Tools"))
    #tools = toolsMenu.Append(my_id, "Align")
    #tools.SetAccel(entry)

    #my_id = wx.NewId()
    #entry = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('2'), my_id)
    #menuBar.Bind(wx.EVT_MENU, Report.Align90, id=my_id)
    #toolsMenu = menuBar.GetMenu(menuBar.FindMenu("Tools"))
    #tools = toolsMenu.Append(my_id, "Align90")
    #tools.SetAccel(entry)

addMenu()

Report().register()
