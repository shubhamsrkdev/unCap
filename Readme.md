# [unCap](https://bitbucket.org/udaykrishna5/uncap/wiki)

## Requirements for dev setup linux
- [Python3](https://www.python.org/downloads/)
- pip3: comes prepackaged with python3 upgrade it
- [kivy](https://kivy.org/docs/installation/installation.html)
- install pillow
```python3 -m pip install pillow```

#### Incase something doesn't work run this
```
#!bash
python3 -m pip install --upgrade pip
python3 -m pip install setuptools
python3 -m pip install Cython
python3 -m pip install wheel
python3 -m pip install requests
python3 -m pip install lxml 
python3 -m pip install pillow
python3 -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python3 -m pip install kivy.deps.gstreamer 
python3 -m pip install kivy
python3 -m pip install psutil

```

> also don't forget to refer to [kivy installation guide](https://kivy.org/docs/installation/installation.html)


## Windows devsetup 
** kivy works only upto python 3.4 on windows so install 3.4 and not 3.6 **

install [microsoft visual studio build tools 2015 and VS 2017](http://landinghub.visualstudio.com/visual-cpp-build-tools)
assuming only python 3 is installed run these commands. In case there's python2 installed as well make sure to replace python with appropriate command that refers to python3
```
python -m pip install --upgrade pip
python -m pip install setuptools
python -m pip install Cython
python -m pip install wheel
python -m pip install requests
python -m pip install lxml 
python -m pip install pillow
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy
python -m pip install psutil

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