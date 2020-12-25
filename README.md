# SC Controller [![Build Status](https://travis-ci.org/b23prodtm/sc-controller.svg?branch=travisobs)](https://travis-ci.org/b23prodtm/sc-controller)
SC Controller

User-mode driver and mapper for Steam Controller, DS4 and similar controllers.

[![screenshot1](docs/screenshot1-tn.png?raw=true)](docs/screenshot1.png?raw=true)
[![screenshot2](docs/screenshot2-tn.png?raw=true)](docs/screenshot2.png?raw=true)
[![screenshot3](docs/screenshot3-tn.png?raw=true)](docs/screenshot3.png?raw=true)
[![screenshot3](docs/screenshot4-tn.png?raw=true)](docs/screenshot4.png?raw=true)

-----------

#### Building

Navigate to directory with sources and use meson to compile:

###### on Linux
```
$ meson build
$ ninja -C build
$ ninja -C build scc-daemon
```

###### on Windows
```
# (you'll need mingw)
$ pacman -S --needed mingw-w64-i686-pkg-config mingw-w64-i686-meson mingw-w64-i686-gcc mingw-w64-i686-python2 mingw-w64-i686-gtk3 mingw-w64-i686-libusb mingw-w64-i686-libmicroutils
$ export PROCESSOR_ARCHITEW6432=x86
$ meson build
$ ninja -C build sc-controller  # start GUI
$ ninja -C build scc-daemon     # start without gui to check why it doesn't work
```

###### on OpenBSD or NetBSD
```
# (install pkg-config, ninja-build and meson packages first. Meson is available as pip package)
$ meson build
$ ninja -C build
$ ninja -C build scc-daemon
```
