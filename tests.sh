#!/bin/bash

# This script will do a simple check for meta information in changed *.md files

file_names=`(git diff --name-only $TRAVIS_COMMIT_RANGE || echo "") | tr '\n' ' '`

for f in $file_names; do
  if [ ! -f "$f" ]; then
    echo "$f : WARNING Is not a file or does not exist anymore."
    continue
  fi
  case $f in
    *.md )
    
    #check for new meta title
    newtitle=$(grep '\.\. title:' $f >> /dev/null 2>&1; echo $?)
    if [[ "$newtitle" != "0" ]]; then
      echo "$f : FAIL Does not contain meta title new see readme"
      fail=1
    fi

    if [[ "$f" =~ [A-Z] ]]; then
       echo "$f : WARNING filepath is not lowercase"
    fi

    title_size=$(grep '\.\. title:' $f | cut -d ':' -f2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | wc -m)
    if [[ "$title_size" == "1" ]]; then
      echo "$f : WARNING Meta title not specified"
    fi
    #Meta title should exclude | UKFast Documentation
    if [[ "$title_size" -gt "43" ]]; then
      echo "$f : WARNING Meta title is $title_size - Max is 42 chars"
    fi

    meta=$(grep '\.\. meta::' $f >> /dev/null 2>&1; echo $?)
    if [[ "$meta" != "0" ]]; then
      echo "$f : WARNING Does not contain meta info"
    fi

    descr_size=$(grep '  :description:' $f | cut -d ':' -f3|wc -m)
    if [[ "$descr_size" == "1" ]]; then
      echo "$f : WARNING Meta description not specified"
    fi
    if [[ "$descr_size" -gt "166" ]]; then
      echo "$f : WARNING Meta description is longer than 165 chars"
    fi
  esac
done

if [[ "$fail" == "1" ]]; then
  exit 1
fi
