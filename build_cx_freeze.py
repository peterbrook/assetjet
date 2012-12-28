import os
import shutil

# Clean the build directory
if os.path.isdir('./build/exe.win-amd64-2.7'):
    shutil.rmtree('./build/exe.win-amd64-2.7')

# Freeze it
os.system('python setup_cx_freeze.py build')

# TODO: Hack - for now, copy over the config file manually
shutil.copy('./assetjet/app.cfg', './build/exe.win-amd64-2.7')