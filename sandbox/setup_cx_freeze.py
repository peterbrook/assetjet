import os, sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
includefiles = []
includes = ['lxml.etree', 'lxml._elementpath',
            'gzip', 'numpy.core._mx_datetime_parser',
            'PySide.QtWebKit', 'web', 'PySide.QtNetwork']
build_exe_options = {'packages': ['pygments', 'os', 'sqlalchemy.dialects.sqlite', 'assetjet'],
                     'icon': '../resources/Pie-chart.ico',
                     'excludes': ['tkinter'],
                     'includes': includes,
                     'include_files': includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(  name = 'assetjet',
        version = '0.1',
        description = 'assetjet',
        options = {'build_exe': build_exe_options},
        executables = [Executable('../app/src/main.py', base=base, targetName="AssetJet.exe")])