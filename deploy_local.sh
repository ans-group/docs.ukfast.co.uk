#!/usr/bin/env bash

docker build -t docslocal .
docker kill docslocal || true
docker rm docslocal || true
docker run --name docslocal -p 80:80 -d docslocal
