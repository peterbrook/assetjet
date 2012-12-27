import sys
from cx_Freeze import setup, Executable
import tn

# Dependencies are automatically detected, but it might need fine tuning.
includefiles = []
includes = ['lxml.etree', 'lxml._elementpath',
            'gzip', 'numpy.core._mx_datetime_parser']
build_exe_options = {'packages': ['os', 'sqlalchemy.dialects.sqlite'],
                     'icon': './resources/Pie-chart.ico',
                     'excludes': ['tkinter'],
                     'includes': includes,
                     'include_files': includefiles}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(  name = 'tripping-nemesis',
        version = tn.__version__,
        description = 'tripping-nemesis is a stock analyzer',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./tn/main.py', base=base)])