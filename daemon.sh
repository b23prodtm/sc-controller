#!/bin/bash

# Set PATH
if [ x"$1" == x"lldb" ] ; then
	shift
	lldb python -- sc-xbox.py $@
else
	python sc-xbox.py $@
fi
