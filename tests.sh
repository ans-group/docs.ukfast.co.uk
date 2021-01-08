#!/bin/bash

# This script will do a simple check for meta information in changed *.md files

log() {
  case $1 in
    "fail" )
      prefix="\033[0;31mFAILURE\033[0m in "
      shift
      ;;
    "warn" )
      prefix="\033[0;33mFAILURE\033[0m in "
      shift
      ;;
  esac
  echo -e "${prefix}${1}: ${2-}"
}

file_names="$@"
changed_files=$(echo $file_names | wc -w)
echo -e "\nChecking ${changed_files} changed files"

for f in $file_names; do

  if [ ! -f "$f" ]; then
    log warn $f "Is not a file or does not exist anymore."
    continue
  fi

  case $f in
    *.md )

      #check for new meta title
      newtitle=$(grep '  \.\. title:: ' $f >> /dev/null 2>&1; echo $?)
      if [[ "$newtitle" != "0" ]]; then
        log fail $f "Does not contain .. title:: <title>. See readme.md"
        fail=1
      fi

      badchars='‘’“”'
      badchars_test=$(grep $'\u2019\|\u2018\|\u201C\|\u201D' $f > /dev/null 2>&1; echo $?)
      if [[ "$badchars_test" == "0" ]]; then
        log fail $f "Invalid characters used. Avoid using any of these: ${badchars}"
        fail=1
      fi

      if [[ "$f" =~ [A-Z] ]]; then
        log warn $f "Filepath is not lowercase"
      fi

      title_size=$(grep '\.\. title:' $f | cut -d ':' -f2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | wc -m)
      #Meta title should exclude | UKFast Documentation
      if [[ "$title_size" -gt "43" ]]; then
        log warn $f "Meta title is $title_size - Max is 42 chars"
      fi

      meta=$(grep '\.\. meta::' $f >> /dev/null 2>&1; echo $?)
      if [[ "$meta" != "0" ]]; then
        log warn $f "Does not contain meta info"
      fi

      descr_size=$(grep '  :description:' $f | cut -d ':' -f3|wc -m)
      if [[ "$descr_size" == "1" ]]; then
        log warn $f "Meta description not specified"
      fi
      if [[ "$descr_size" -gt "166" ]]; then
        log warn $f "Meta description is longer than 165 chars"
      fi
  esac
done

if [[ "$fail" == "1" ]]; then
  exit 1
fi
