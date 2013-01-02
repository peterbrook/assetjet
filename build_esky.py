from subprocess import call

# Freeze it and produce patches in case older versions are in the directory
call('python setup_esky.py bdist_esky_patch')
