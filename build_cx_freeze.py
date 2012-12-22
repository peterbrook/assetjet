import os
import shutil

# Clean the build directory
if os.path.isdir('build'): shutil.rmtree('build')

# Freeze it
os.system('python setup_cx_freeze.py build')