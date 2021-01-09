#!/usr/bin/env bash
[ $# -lt 2 ] && echo "Usage: $0 <subfolder> <wildcard>" && exit 1
w=`pwd`
folder="$1"
cd "$folder" || exit 1
while [ $# -gt 1 ]; do
  shift
  wildcard="$1"
  for i in $wildcard; do
      echo "$folder/$i"
  done
done
cd "$w" || exit 1
