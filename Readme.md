# [unCap](https://bitbucket.org/udaykrishna5/uncap/wiki)

## Requirements for dev setup linux
- [Python3](https://www.python.org/downloads/)
- pip3: comes prepackaged with python3 upgrade it
- [kivy](https://kivy.org/docs/installation/installation.html) ``` pip install 
- install pillow
```python3 -m pip install pillow```

#### Incase something doesn't work run this
```
python3 -m pip install --upgrade pip
python3 -m pip install setuptools
python3 -m pip install Cython
python3 -m pip install wheel
python3 -m pip install requests
python3 -m pip install lxml 
python3 -m pip install pillow

```


## Windows devsetup 
** kivy works only upto python 3.4 on windows so install 3.4 and not 3.6 **

install [microsoft visual studio build tools 2015 and VS 2017](http://landinghub.visualstudio.com/visual-cpp-build-tools)

```
python -m pip install --upgrade pip
python -m pip install setuptools
python -m pip install Cython
python -m pip install wheel
python -m pip install requests
python -m pip install lxml 
python -m pip install pillow

```
use wheel for lxml if it fails [download link of wheel](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml)

python -m pip wheel <name of the wheel downloaded>




## running unCap
```
#!bash
git clone git@bitbucket.org:udaykrishna5/uncap.git
cd uncap
python3 main.py
```