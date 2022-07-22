# Swap Components

KiCad plugin to swap two footprints in Pcbnew.

Select two (or more) footprints, and hit the toolbar icon, and the footprints will swap locations.

If more than two components are selected then the location information of them will be transferred to the next one in the list, rotated around from the end to the start again.

## Installation

- Copy `swap_components.py` into your KiCad plugin folder
- On my computer, using KiCad 5, it's `C:\Users\<username>\AppData\Roaming\kicad\scripting\plugins`
- On my computer, using KiCad 6, it's `C:\Users\<username>\Documents\KiCad\6.0\scripting\plugins`
- In KiCad 6, you can go to `Tools->External Plugins->Open Plugins Directory` for your particular setup
