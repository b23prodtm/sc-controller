#!/bin/bash

# Set PATH
SCRIPTS="$(pwd)/scripts"
export PATH="$SCRIPTS":"$PATH"
export PYTHONPATH=".":"$PYTHONPATH"
export SCC_SHARED="$(pwd)"

if [ x"$1" == x"lldb" ] ; then
	shift
	lldb python -- 'scripts/scc-daemon' debug $@
else
	python 'scripts/scc-daemon' $@
fi
