#!/usr/bin/env bash
cd "$MESON_SOURCE_ROOT" || exit 1
python3 setup.py build
python3 setup.py install
