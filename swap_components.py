"""
Swaps the location of two selected components
"""
import pcbnew

class ComponentSwap(pcbnew.ActionPlugin):
    """
    Select two (or more!) components and press the button
    """
    def defaults(self):
        self.name = "Swap the location of components"
        self.category = "Modify PCB"
        self.description = "Swap the coordinates of selected components"
        self.show_toolbar_button = True

    def Run(self):
        pcb = pcbnew.GetBoard()
        
        kicad5 = pcbnew.GetBuildVersion().startswith('5')
        
        #
        selectedMods = []
        
        if kicad5:
            for mod in pcb.GetModules():
                if mod.IsSelected():
                    selectedMods.append(mod)
        else:
            for mod in pcb.GetFootprints():
                if mod.IsSelected():
                    selectedMods.append(mod)
                
        length = len(selectedMods)
        newPos = []
        
        for i in range(length):
            pos = selectedMods[i].GetPosition()
            orient = selectedMods[i].GetOrientation()
            layer = selectedMods[i].GetLayer()
            flip = selectedMods[i].IsFlipped()
            param = { 'pos': pos, 'orient': orient, 'layer': layer, 'flip': flip }
            newPos.append(param)
            
        newPos = newPos[1:] + newPos[:1]
            
            
        for i in range(length):
            selectedMods[i].SetPosition(newPos[i]['pos'])
            selectedMods[i].SetOrientation(newPos[i]['orient'])
            selectedMods[i].SetLayer(newPos[i]['layer'])
            # if selectedMods[i].IsFlipped() && !newPos[i]['flip']
            
        pcbnew.Refresh()
            
                


ComponentSwap().register()
