import os
import shutil

# Clean the build directory
if os.path.isdir('./build/exe.win-amd64-2.7'):
    shutil.rmtree('./build/exe.win-amd64-2.7')

# Freeze it
os.system('python setup_cx_freeze.py build')

# TODO: copy over web folder and local_server.py


