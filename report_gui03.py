import pcbnew
import csv
import wx
import os
from wx.lib.scrolledpanel import ScrolledPanel

'''
exec(open('/home/quantum/Desktop/git_repo/kicad/report_gui03.py').read())
'''
label_list = []

### Functions definition ###
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

def get_component_info():
    board = pcbnew.GetBoard()
    front_tht = 0
    back_tht  = 0
    front_smd = 0
    back_smd  = 0
    smd_pads  = 0
    tht_pads  = 0

    for module in board.GetModules():
        smd = 0
        for pad in module.Pads():
            if(pad.GetAttribute()):
                smd = 1
                smd_pads += 1
            else:
                tht_pads += 1
        if(smd == 1):
            if(module.IsFlipped()):
                back_smd  += 1
            else:
                front_smd += 1
        else:
            if(module.IsFlipped()):
                back_tht  += 1
            else:
                front_tht += 1
    print(front_tht, back_tht, front_smd, back_smd)
    return [front_tht, back_tht, front_smd, back_smd, smd_pads, tht_pads]

def get_via_info():
    return [1, 0, 10]

def get_board_info():
    return [58.5, 90.5]

### Panel definition ###
app = wx.App()
frame = wx.Frame(parent=None, title="Report", size=(900, 900))

panel01 = ScrolledPanel(frame)
panel01.SetupScrolling()
vbox01 = wx.BoxSizer(wx.VERTICAL)

### Components ###
hbox02 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox02, panel01, "Components", (120, 20))
vbox01.Add(hbox02)

[front_tht, back_tht, front_smd, back_smd, SMD, through_hole] = get_component_info()

hbox03 = wx.BoxSizer(wx.HORIZONTAL)
header01 = ["\t", 'Front Side', 'Back Side', 'Total']
for header in header01:
    add_label(hbox03, panel01, header)
vbox01.Add(hbox03)

hbox04 = wx.BoxSizer(wx.HORIZONTAL)
header02 = ['THT: ', front_tht, back_tht]
header02.append((header02[1]+header02[2]))
for header in header02:
    add_label(hbox04, panel01, str(header))
vbox01.Add(hbox04)

hbox05 = wx.BoxSizer(wx.HORIZONTAL)
header03 = ['SMD: ', front_smd, back_smd]
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

[connector, NPTH] = [0, 10]

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

[board_width, board_height] = get_board_info()
hbox14 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox14, panel01, 'Width:')
add_label(hbox14, panel01, str(board_width))
vbox03.Add(hbox14)

hbox15 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox15, panel01, 'Height:')
add_label(hbox15, panel01, str(board_height))
vbox03.Add(hbox15)

hbox16 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox16, panel01, 'Area:')
add_label(hbox16, panel01, str(board_height*board_width))
vbox03.Add(hbox16)

### Vias ###
vbox04 = wx.BoxSizer(wx.VERTICAL)

hbox17 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox17, panel01, 'Vias')
vbox04.Add(hbox17)

[through, blind, micro] = get_via_info()
hbox18 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox18, panel01, 'Through vias:')
add_label(hbox18, panel01, str(through))
vbox04.Add(hbox18)

hbox19 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox19, panel01, 'Blind/buried:')
add_label(hbox19, panel01, str(blind))
vbox04.Add(hbox19)

hbox20 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox20, panel01, 'Micro vias:')
add_label(hbox20, panel01, str(micro))
vbox04.Add(hbox20)

hbox21 = wx.BoxSizer(wx.HORIZONTAL)
add_label(hbox21, panel01, 'Total:')
add_label(hbox21, panel01, str(micro+blind+through))
vbox04.Add(hbox21)

### Final UI ###
hbox_02 = wx.BoxSizer(wx.HORIZONTAL)
hbox_02.Add(vbox03)
hbox_02.Add(vbox04)

vbox05 = wx.BoxSizer(wx.VERTICAL)
vbox05.Add(hbox_01)
vbox05.Add(hbox_02)

panel01.SetSizer(vbox05)
frame.Show()
app.MainLoop()
