import pcbnew
import csv
import wx
import os
from wx.lib.scrolledpanel import ScrolledPanel

'''
exec(open('/home/quantum/Desktop/git_repo/kicad/report_gui01.py').read())
'''
label_list = []

def get_comp():
    board = pcbnew.GetBoard()
    ref = []
    for comp in board.GetModules():
        ref.append(comp.GetReference())
    return ref

def add_label(box, panel, label_name):
    label_list.append(wx.StaticText(panel, -1, style=wx.ALIGN_CENTER, size=(200, 20)))
    label_list[-1].SetLabel(label_name)
    box.Add(label_list[-1], 0, wx.ALIGN_CENTER)

app = wx.App()
frame = wx.Frame(parent=None, title="Report", size=(900, 900))

panel01 = ScrolledPanel(frame)
panel01.SetupScrolling()
vbox01 = wx.BoxSizer(wx.VERTICAL)

hbox02 = wx.BoxSizer(wx.HORIZONTAL)
vbox01.Add(hbox02)

references = get_comp()
for reference in references:
    add_label(vbox01, panel01, reference)
    add_label(hbox02, panel01, reference)
panel01.SetSizer(vbox01)
frame.Show()
app.MainLoop()
