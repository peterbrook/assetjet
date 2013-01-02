import os, sys, time
from esky.bdist_esky import Executable
from distutils.core import setup
from glob import glob
from deploy import package


if sys.platform in ['win32','cygwin','win64']:
	#    data_files = [("images", glob(r'.\images\*.*'))]
	#  We can customise the executable's creation by passing an instance
    #  of Executable() instead of just the script name.
    example = Executable("../../assetjet/main.py",
                        icon='../../resources/Pie-chart.ico',
                        gui_only=True,
                        name="AssetJet.exe"
                        )

    setup(
      name = package.AppName,
      version = package.GetVersionString(),
      scripts = [example],
      options = {"bdist_esky":{
                 #  forcibly include some other modules
                 "includes": ['lxml.etree', 'lxml._elementpath',
                              'gzip', 'numpy.core._mx_datetime_parser'],
                 #  forcibly exclude some other modules
                 "excludes": ['tkinter', 'pydoc'],
                 #  force esky to freeze the app using py2exe
                 "freezer_module": "cx_freeze",
                 #  tweak the options used by cx_freezer
                 "freezer_options":  {'packages': ['os', 'sqlalchemy.dialects.sqlite']}
              }}
    )

