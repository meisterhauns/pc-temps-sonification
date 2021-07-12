# Sonification of Computer Temperatures

## Requirements

- Python 3
- Packages [wmi](https://pypi.org/project/WMI/), [numpy](https://pypi.org/project/numpy/), [sounddevice](https://pypi.org/project/sounddevice/), [matplotlib](https://pypi.org/project/matplotlib/) and [soundfile](https://pypi.org/project/soundfile/) (all installable via _pip install __package_name___)
- (optional) [VS Code](https://code.visualstudio.com/) to work with the interactive mode (Comments starting with __# %%__)


## Setup

- Clone the repository
- To monitor your own system: 
  - Download [OpenHardwareMonitor](https://openhardwaremonitor.org/downloads/)
  - Unpack everything into the directory of the repository
  - Sometimes Windows disables the dll. To solve this:
    
    _Right click_ -> _Properties_ -> Section _Attributes_ at the bottom
    
    If there are only options for _Read only_ and _Hidden_ you're good, otherwise click the option to enable it

## Running [monitor.py](https://github.com/meisterhauns/pc-temps-sonification/blob/main/monitor.py)

- Before starting the script run _OpenHardwareMonitor.exe_ and let it run in the background
- Open [data.csv](https://github.com/meisterhauns/pc-temps-sonification/blob/main/data.csv) and clear the contents
- You can try to run it now or customize the script to fit your Hardware - open it up to read more
- This can / should be run from the console as this will probably stay in the background for a few hours
  
  You can resume collecting data anytime because it just appends the data to the csv (again, clear the file contents before running it with your customized version!)

## Running [sonification.py](https://github.com/meisterhauns/pc-temps-sonification/blob/main/sonification.py)

- It's highly recommended to use it in interactive mode (needs [VS Code](https://code.visualstudio.com/) (Comments starting with __# %%__))
- If you created your own [data.csv](https://github.com/meisterhauns/pc-temps-sonification/blob/main/data.csv) then exchange the columns in the array loading section and add or remove lines depending on how many and which PC parts you want to hear.
- Have fun listenting!