import sys
from esky.bdist_esky import Executable
from distutils.core import setup
import assetjet
from main import exeName, appName
from glob import glob

if sys.platform in ['win32','cygwin','win64']:
    
    # TODO: add folder contents recursively
    data_files = [("web", glob('../../app/src/web/*.*')),
                  ("web/res", glob('../../app/src/web/res/*.*'))
                  ]
    
    # We can customise the executable's creation by passing an instance
    # of Executable() instead of just the script name.
    exe = Executable('../../app/src/main.py',
                     icon='../../resources/Pie-chart.ico',
                     gui_only=True,
                     name=exeName
                    )

    setup(
      data_files = data_files,
      name = appName,
      version = assetjet.__version__,
      scripts = [exe],
      options = {'bdist_esky':{
                 #  forcibly include some other modules
                 'includes': ['lxml.etree', 'lxml._elementpath',
                              'gzip', 'numpy.core._mx_datetime_parser'],
                 #  forcibly exclude some other modules
                 'excludes': ['tkinter', 'pydoc'],
                 #  force esky to freeze the app using py2exe
                 'freezer_module': 'cx_freeze',
                 #  tweak the options used by cx_freezer
                 'freezer_options':  {'packages': ['os', 'sqlalchemy.dialects.sqlite']}
              }}
    )

