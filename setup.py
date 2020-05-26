#make_exe.py
from cx_Freeze import setup,Executable
import sys
 
# Replaces commandline arg 'build'
#sys.argv.append("build")
 
# If need to include/exclude module/packages
icon = 'images\icon.ico'
includes = []
excludes = []
packages = []
include_files = ['promemoria.db','images']
 
# Console or Win32GUI
base = None
if sys.platform == "win32":
    #base = 'Console'
    base = 'Win32GUI'
 
# Name of file to make ".exe" of
filename = "Consulta de Obitos.py"
setup(
    name = 'Myapp',
    version = '0.1',
    description = 'Cx test',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'includes':includes, 'include_files':include_files}},
    executables = [Executable(filename, base=base, icon = icon)])
 
# From command line
#python make_exe.py build