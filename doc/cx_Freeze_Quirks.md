### NumPy 1.7.0

comment out "del sys" in /numpy/core/init.py  
http://stackoverflow.com/questions/14969552/error-when-freezing-pandas-numpy-1-7-0-code-with-cx-freeze
  
there's a patch available here to fix this issue in cx_Freeze:  
http://sourceforge.net/p/cx-freeze/bugs/36/

### Chameleon

in chameleon-2.9.2-py2.6.egg/chameleon/codegen.py, replace

source = textwrap.dedent(inspect.getsource(function))  
with  
source = textwrap.dedent('')  
http://www.mail-archive.com/cx-freeze-users@lists.sourceforge.net/msg01284.html

### Print statments

get rid of all print statements or otherwise the frozen app will fail with something like Error9: File not found.
