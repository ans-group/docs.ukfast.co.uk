FROM python:3.8-alpine as builder

RUN pip install Sphinx recommonmark && \
    apk add build-base git

WORKDIR /build

ADD Makefile rasterize.js ./
ADD source ./source/

RUN make clean && \
    sphinx-build -n -b html -d build/doctrees source/ build/html && \
    make build/html/_static/css/app.css && \
    make build/html/_static/app.js

FROM nginx:stable

RUN apt update && \
    apt install curl -y

# Grab the resources from the python builder so we can bin it off.
COPY --from=builder /build/build/html /usr/share/nginx/docs.ukfast.co.uk/html
COPY /nginx/nginx.conf /etc/nginx/nginx.conf
