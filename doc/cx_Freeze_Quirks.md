### NumPy 1.7.0

Workaround: comment out "del sys" in /numpy/core/init.py  
http://stackoverflow.com/questions/14969552/error-when-freezing-pandas-numpy-1-7-0-code-with-cx-freeze
  
There's a patch available here to fix this issue in cx_Freeze:  
http://sourceforge.net/p/cx-freeze/bugs/36/

### Chameleon

in chameleon-2.9.2-py2.6.egg/chameleon/codegen.py, replace

source = textwrap.dedent(inspect.getsource(function))  
with  
source = textwrap.dedent('')  
http://www.mail-archive.com/cx-freeze-users@lists.sourceforge.net/msg01284.html

### Print statements

get rid of all print statements or otherwise the frozen app will fail with something like Error9: File not found.

### Icons (resource files)

Add this to cx_Freeze/hooks.py:

    def load_PySide_QtGui(finder, module):
        """There is a chance that GUI will use some image formats
        add the image format plugins
        """
        dir0 = os.path.dirname(module.file)
        dir = os.path.join(dir0, "plugins", "imageformats")
        finder.IncludeFiles(dir, "imageformats")

https://bitbucket.org/anthony_tuininga/cx_freeze/pull-request/11/added-pyqt4qtgui-load-hook-that-adds/diff#comment-134053

NOTE: Since Esky needs the folder next to the called executable, we don't need this in AssetJet, but rather copy the file seperately.
