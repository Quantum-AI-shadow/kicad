import pcbnew
import csv
import wx
import os

class Report(pcbnew.ActionPlugin):
    def defaults(self):
        self.name        = "Align"
        self.category    = "Modify PCB"
        self.description = "Align the selected component to 0 degree"
        
    def Run(self):
        board       = pcbnew.GetBoard()
        for comp in board.GetModules():
            if(comp.IsSelected()):
                comp.SetOrientation(0)
        pcbnew.Refresh()

windows    = wx.GetTopLevelWindows()
pcbwindow  = list(filter(lambda w: 1, windows))
menuBar = pcbwindow[2].MenuBar

my_id = wx.NewId()
entry = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('W'), my_id)
menuBar.Bind(wx.EVT_MENU, Report.Run, id=my_id)
pluginMenu = wx.Menu()
newitem = wx.MenuItem(pluginMenu, wx.ID_NEW, text="Plugins", kind=wx.ITEM_NORMAL)
tools   = pluginMenu.Append(my_id, "Align")
menuBar.Append(pluginMenu, '&Plugins')
#toolsMenu = menuBar.GetMenu(menuBar.FindMenu("Tools"))
#tools = toolsMenu.Append(my_id, "Align")
tools.SetAccel(entry)

Report().register()
