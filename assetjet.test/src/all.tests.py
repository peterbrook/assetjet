import unittest
import os, sys





testdir = os.curdir

suite = unittest.TestLoader().discover(testdir, "*test.py")
unittest.TextTestRunner(verbosity=2).run(suite)
