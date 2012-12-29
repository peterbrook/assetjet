from subprocess import call

# Freeze it
call('python setup_esky.py bdist_esky')

#call('python setup_esky.py bdist_esky_patch')