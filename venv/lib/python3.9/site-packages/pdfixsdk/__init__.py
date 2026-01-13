__version__="8.7.9"

from .Pdfix import *

import platform, os
from ctypes import cdll

# get the shared library name based on the platform
def getModuleName(module):
  machine = platform.uname().machine
  pltfm = platform.system()
  if pltfm == 'Darwin':
    if machine == "arm64":
      return 'arm64/lib' + module + '.dylib'  
    else:
      return 'x86_64/lib' + module + '.dylib'
  elif pltfm == "Windows":
    if machine == "arm64":
      return 'arm64/' + module + '.dll'  
    else:
      return 'x86_64/' + module + '.dll'
  elif pltfm == "Linux":
    if machine == "aarch64":
      return 'aarch64/lib' + module + '.so'  
    else:
      return 'x86_64/lib' + module + '.so'
  
# load pdfix library from the current folder
basePath = os.path.dirname(os.path.abspath(__file__))
Pdfix_init(basePath + "/bin/" + getModuleName('pdf'))

# load additional dependencies
if platform.system() == "Windows":
  cdll.LoadLibrary(basePath + "/bin/" + getModuleName("LicenseSpringVMD"))
