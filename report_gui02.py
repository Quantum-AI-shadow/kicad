import pcbnew
import csv
import wx
import os
from wx.lib.scrolledpanel import ScrolledPanel

'''
exec(open('/home/quantum/Desktop/git_repo/kicad/report_gui02.py').read())
'''
label_list = []

def get_comp():
    board = pcbnew.GetBoard()
    ref = []
    for comp in board.GetModules():
        ref.append(comp.GetReference())
    return ref

def add_label(box, panel, label_name, size_label=(100,20)):
    label_list.append(wx.StaticText(panel, -1, style=wx.ALIGN_CENTER, size=size_label))
    label_list[-1].SetLabel(label_name)
    box.Add(label_list[-1], 0, wx.ALIGN_CENTER)

def get_component_THT():
    return [28, 1]

def get_component_SMD():
    return [0,1]

def get_pads_detail():
    return [97, 0, 1, 2]

app = wx.App()
frame = wx.Frame(parent=None, title="Report", size=(900, 900))

panel01 = ScrolledPanel(frame)
panel01.SetupScrolling()
vbox01 = wx.BoxSizer(wx.VERTICAL)

### Components ###
hbox02 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox02, panel01, "Components", (120, 20))
vbox01.Add(hbox02)

hbox03 = wx.BoxSizer(wx.HORIZONTAL)
header01 = ["\t", 'Front Side', 'Back Side', 'Total']
for header in header01:
    add_label(hbox03, panel01, header)
vbox01.Add(hbox03)

hbox04 = wx.BoxSizer(wx.HORIZONTAL)
header02 = ['THT: ', get_component_THT()[0], get_component_THT()[1]]
header02.append((header02[1]+header02[2]))
for header in header02:
    add_label(hbox04, panel01, str(header))
vbox01.Add(hbox04)

hbox05 = wx.BoxSizer(wx.HORIZONTAL)
header03 = ['SMD: ', get_component_SMD()[0], get_component_SMD()[1]]
header03.append((header03[1]+header03[2]))
for header in header03:
    add_label(hbox05, panel01, str(header))
vbox01.Add(hbox05)

hbox06 = wx.BoxSizer(wx.HORIZONTAL)
header04 = ['Total: ', header02[1]+header03[1], header02[2]+header03[2]]
header04.append((header04[1]+header04[2]))
for header in header04:
    add_label(hbox06, panel01, str(header))
vbox01.Add(hbox06)

### Pads ###
vbox02 = wx.BoxSizer(wx.VERTICAL)

hbox07 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox07, panel01, 'Pads', (50, 20))
vbox02.Add(hbox07)

[through_hole, SMD, connector, NPTH] = get_pads_detail()

hbox08 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox08, panel01, 'Through hole:')
add_label(hbox08, panel01, str(through_hole))
vbox02.Add(hbox08)

hbox09 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox09, panel01, 'SMD:')
add_label(hbox09, panel01, str(SMD))
vbox02.Add(hbox09)

hbox10 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox10, panel01, 'Connector:')
add_label(hbox10, panel01, str(connector))
vbox02.Add(hbox10)

hbox11 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox11, panel01, 'NPTH:')
add_label(hbox11, panel01, str(NPTH))
vbox02.Add(hbox11)

hbox12 = wx.BoxSizer(wx.HORIZONTAL)
Total_pads = NPTH + connector + SMD + through_hole
add_label(hbox12, panel01, 'Total:')
add_label(hbox12, panel01, str(Total_pads))
vbox02.Add(hbox12)

hbox_01 = wx.BoxSizer(wx.HORIZONTAL)
hbox_01.Add(vbox01)
hbox_01.Add(vbox02)

### Board size ###
vbox03 = wx.BoxSizer(wx.VERTICAL)

hbox13 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox13, panel01, 'Board size')
vbox03.Add(hbox13)

vbox04 = wx.BoxSizer(wx.VERTICAL)

hbox14 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox14, panel01, 'Vias')
vbox04.Add(hbox14)

hbox_02 = wx.BoxSizer(wx.HORIZONTAL)
hbox_02.Add(vbox03)
hbox_02.Add(vbox04)

vbox05 = wx.BoxSizer(wx.VERTICAL)
vbox05.Add(hbox_01)
vbox05.Add(hbox_02)

panel01.SetSizer(vbox05)
frame.Show()
app.MainLoop()
