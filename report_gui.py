import pcbnew
import csv
import wx
import os
from wx.lib.scrolledpanel import ScrolledPanel

'''
exec(open('/home/quantum/Desktop/git_repo/kicad/report_gui.py').read())
'''
label_list = []

def get_comp():
    board = pcbnew.GetBoard()
    ref = []
    for comp in board.GetModules():
        ref.append(comp.GetReference())
    return ref

def add_label(label_name):
    label_list.append(wx.StaticText(panel, -1, style=wx.ALIGN_CENTER, size=(200, 20)))
    label_list[-1].SetLabel(label_name)
    my_sizer.Add(label_list[-1], 0, wx.ALIGN_CENTER)

app = wx.App()
frame = wx.Frame(parent=None, title="Report", size=(900, 900))
panel = ScrolledPanel(frame)
panel.SetupScrolling()
my_sizer = wx.BoxSizer(wx.VERTICAL)

references = get_comp()
for reference in references:
    add_label(reference)
panel.SetSizer(my_sizer)
frame.Show()
app.MainLoop()
