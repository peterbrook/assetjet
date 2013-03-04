import sys, os
from esky.bdist_esky import Executable
from distutils.core import setup
import assetjet
from deploy import exeName, appName
from glob import glob

def get_data_files(dirs):
    """
    Recursively include data directories.
    """
    results = []
    for directory in dirs:
        for root, dirs, files in os.walk(directory):
            files = [os.path.join(root, file_) for file_ in files]
            targetdir = os.path.relpath(root, os.path.join(directory, os.path.pardir))
            results.append((targetdir, files))
    return results

if sys.platform in ['win32','cygwin','win64']:
    
    # Add http files
    data_files =  get_data_files([r'../app/src/httpdocs']) + [
                  r'../app/src/local_server.pyc']
    
    # We can customise the executable's creation by passing an instance
    # of Executable() instead of just the script name.
    exe = Executable('../app/src/main.py',
                     icon='../resources/images/Pie-chart.ico',
                     gui_only=True,
                     name=exeName,                     
                    )

    setup(
      data_files = data_files,
      name = appName,
      version = assetjet.__version__,
      scripts = [exe],
      options = {'bdist_esky':{
                 #  forcibly include some other modules
                 'includes': ['lxml.etree', 'lxml._elementpath',
                              'gzip','numpy',
                              'PySide.QtWebKit', 'PySide.QtNetwork', 'PySide.QtSvg'],
                 #  forcibly exclude some other modules
                 'excludes': ['Tkinter', 'Tkconstants', 'pydoc', 'tcl', 'tk', 'matplotlib', 'PIL', 'nose', 'setuptools', 'xlrd', 'xlwt', 'PyQt4', 'markdown', 'IPython', 'docutils'],
                 #  force esky to freeze the app using py2exe
                 'freezer_module': 'cx_freeze',
                 #  tweak the options used by cx_freezer
                 'freezer_options':  {'packages': ['pygments', 'sqlalchemy.dialects.sqlite', 'assetjet']}
              }}
    )

