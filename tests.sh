#!/bin/bash

# This script will do a simple check for meta information in changed *.md files

file_names=`(git diff --name-only $TRAVIS_COMMIT_RANGE || echo "") | tr '\n' ' '`

for f in $file_names; do
  if [ ! -f "$f" ]; then
    echo "$f : Is not a file or does not exist anymore."
    continue
  fi
  case $f in
    *.md )
    meta=$(grep '\.\. meta::' $f >> /dev/null 2>&1; echo $?)
    if [[ "$meta" != "0" ]]; then
      echo "$f : Does not contain meta info"
      fail=1
    fi
  esac
done

if [[ "$fail" == "1" ]]; then
  exit 1
fi
