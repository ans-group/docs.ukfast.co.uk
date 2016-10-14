#!/bin/bash
cd /opt/docs.ukfast.co.uk
git submodule update --init
git pull --recurse-submodules origin master
cd ukf && git pull origin master && cd -
curl -XDELETE 'http://localhost:9200/documentation/'
make populate-index
