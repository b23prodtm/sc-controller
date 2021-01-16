#!/usr/bin/env python

import sys
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
import glob

uinput = Extension('libuinput',
                   sources = ['src/uinput.c'])

deps = ['libusb1', 'psutil']
if sys.version_info < (3,4):
    deps.append('enum34')

data_files = [
				('share/pixmaps', [ "images/sc-controller.svg" ]),
				('share/applications', ['scripts/sc-controller.desktop' ]),
				('lib/udev/rules.d', glob.glob('scripts/*.rules')),
]

setup(name='python-steamcontroller',
      version='0.5',
      description='Steam Controller userland driver',
      author='Bno Rk Tina',
      author_email='b23prodtm@users.sourceforge.net',
      url='https://github.com/b23prodtm/sc-controller',
      package_dir={'steamcontroller': 'src'},
      packages=['steamcontroller'],
      data_files=data_files,
      scripts=['scripts/sc-dump.py',
               'scripts/sc-xbox.py',
               'scripts/sc-desktop.py',
               'scripts/sc-mixed.py',
               'scripts/sc-test-cmsg.py',
               'scripts/sc-gyro-plot.py',
               'scripts/vdf2json.py',
               'scripts/json2vdf.py'],
      license='MIT',
      platforms=['Linux'],
      install_requires=deps,
      ext_modules=[uinput, ])
