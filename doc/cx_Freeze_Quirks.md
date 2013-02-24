## NumPy 1.7.0

* comment out "del sys" in /numpy/core/init.py
[source](http://stackoverflow.com/questions/14969552/error-when-freezing-pandas-numpy-1-7-0-code-with-cx-freeze)

## Chameleon

* in chameleon-2.9.2-py2.6.egg/chameleon/codegen.py, replace

source = textwrap.dedent(inspect.getsource(function))
with
source = textwrap.dedent('')

[source](http://www.mail-archive.com/cx-freeze-users@lists.sourceforge.net/msg01284.html)
