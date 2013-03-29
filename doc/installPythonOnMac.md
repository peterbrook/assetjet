# How to install Python with scientific packages on a Mac (Mountain Lion)

## [1] Xcode
* Install Xcode from the AppStore.
* Run it, then select "Create a new Xcode project"
* Under Xcode/Preferences, install the Command Line Tools. You may have to repeat the last step after every Xcode update. 

## [2] Homebrew
* Install Homebrew by pasting the following at a Terminal prompt:  
`ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"`
* Run `brew update`
* Run `brew doctor` and google/fix all the messages
* You may have to edit the path order by running `sudo vi /etc/paths` to make sure that `usr/local/bin` (the location of the brewed Python) appears before `/usr/bin` (if unfamiliar with vim: google vim commands)

## [3] Python
`brew install python --framework --universal`

## [4] Optional: virtualenv/virtualenvwrapper
* untested, since installing numpy/scipy on a mac almost certainly fails with the standard pip install

```
    pip install virtualenv
    pip install virtualenvwrapper
    source /usr/local/share/python/virtualenvwrapper.sh
    mkvirtualenv <virtualenvname>
    workon <virtualenvname>
````

## [5] Packages

* using virtualenv, the installation of the pip-installed-packages could be automated with a bootstrap script
* Some of the packages will install additional packages  (dependencies)
* For dev version of a brew install add `--devel` or `--HEAD`
* Note that the brew commands need to be installed outside of any virtualenv! Use virtuelenv for pip installs only!

```
    brew tap samueljohn/python
    brew install numpy
    brew install gfortran
    brew install scipy
    brew install pyside  
    
    pip install matplotlib
    pip install sphinx
    pip install nose
    pip install spyder
    pip install pyramid
    pip install pandas
    pip install sqlalchemy
    pip install esky
    pip install lxml
```

For cx_Freeze, download the source tarball, unzip and run `python setup.py install`

## [6] Upgrades
    brew upgrade <packagename>
    pip install <packagename> --upgrade

## [7] Uninstalls
    brew uninstall <packagename>
    pip uninstall <packagename>
    rmvirtualenv <virutalenvname>

## [8] Links/Sources
http://www.thisisthegreenroom.com/2011/installing-python-numpy-scipy-matplotlib-and-ipython-on-lion  
http://mxcl.github.com/homebrew  
https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python  
https://github.com/samueljohn/homebrew-python  
http://www.virtualenv.org  
http://www.pip-installer.org
