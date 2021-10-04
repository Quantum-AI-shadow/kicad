import pcbnew
from pcbnew import *

'''
exec(open('/home/quantum/Desktop/git_repo/kicad/create.py').read())

'''

def get_component(name):
    return [x for x in board.GetModules() if x.GetReference() == name][0]

def getnetID(netName):
    nets    = board.GetNetsByName()
    netCode = nets.find(netName).value()[1].GetNet()
    return netCode

def addVia(x, y, drill, width, netName, refresh = 1):
    newVia = pcbnew.VIA(board)
    newVia.SetPosition(pcbnew.wxPoint(x*1e6, y*1e6))
    newVia.SetDrill(int(drill*1e6))
    newVia.SetWidth(int(width*1e6))
    newVia.SetNetCode(getnetID(netName))
    board.Add(newVia)
    if(refresh == 1):
        pcbnew.Refresh()
