#!/usr/bin/env bash
[ -z "$MESON_BUILD_ROOT" ] && MESON_BUILD_ROOT=build
meson "$MESON_BUILD_ROOT" || exit 1
ninja -C "$MESON_BUILD_ROOT" || exit 1
kill_it() {
	taskkill -F -IM "$IM.exe"
}
	
if [ "$(uname)" = .*MINGW??_NT.* ]; then
	export SCC_SHARED="$MESON_BUILD_ROOT\\..\\"
	PATHS="%PATH%"
	PATHS="%CD%\\src\\client;$PATHS"
	PATHS="%CD%\\src\\osd\\common;$PATHS"
	PATHS="%CD%\\src\\osd\\menus;$PATHS"
	PATHS="%CD%\\src\\virtual-device;$PATHS"
	EXE="$(echo "$1" | tr \"/\" \"\\\\\").exe"
	export IM="$(echo "$1" | rev | cut -d / -f 1 | rev)"
	shift
	PARS="$(echo $@ | tr \"/\" \"\\\\\")"
	
	trap kill_it SIGINT
	
	echo "Working directory: $(pwd)"
	cmd.exe /C "set PATH=$PATHS & $EXE $PARS"
	exit $?
else
	cd "$MESON_BUILD_ROOT" || exit 1
	export SCC_SHARED="$MESON_BUILD_ROOT/.."
	export PYTHON_PATH="$MESON_BUILD_ROOT/../python"
	$@
	exit $?
fi

