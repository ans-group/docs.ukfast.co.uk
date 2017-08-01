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
    title_size=$(grep '  :title:' $f | cut -d ':' -f3|wc -m)
    if [[ "$title_size" -gt "66" ]]; then
      echo "$f : Meta title is longer than 65 chars"
    fi
    descr_size=$(grep '  :description:' $f | cut -d ':' -f3|wc -m)
    if [[ "$descr_size" -gt "166" ]]; then
      echo "$f : Meta description is longer than 165 chars"
    fi
  esac
done

if [[ "$fail" == "1" ]]; then
  exit 1
fi
