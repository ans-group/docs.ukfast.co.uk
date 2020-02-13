#FROM python:3.7-slim as builder
#FROM python:2-alpine as builder
FROM python:3.8-alpine as builder

RUN pip install Sphinx recommonmark
RUN apk add build-base
#RUN apt update
#RUN apt install make -y

WORKDIR /build/

ADD Makefile rasterize.js tests.sh /build/
ADD ./files/ ./files/
# ADD ./ukf/ ./ukf/
# Do two copies, the above wont change much, adds a layer but saves time
ADD ./source/ ./source/

RUN make clean && \
    sphinx-build -n -b html -d build/doctrees source/ build/html && \
    make build/html/_static/css/app.css && \
    make build/html/_static/app.js


FROM nginx:stable

RUN apt update
RUN apt install curl -y

# RUN mkdir /usr/share/nginx/docs.ukfast.co.uk
# RUN mkdir /usr/share/nginx/search-docs.ukfast.co.uk
# RUN mkdir /usr/share/nginx/search.docs.ukfast.co.uk
# RUN mkdir /usr/share/nginx/docs.ukfast.co.uk/logs

# Grab the resources from the python builder so we can bin it off.
COPY --from=builder /build/build/html /usr/share/nginx/docs.ukfast.co.uk/html

COPY /nginx/nginx.conf /etc/nginx/nginx.conf

# Get the nginx confs in there.
# COPY /nginx/docs-search.ukfast.co.uk.conf /etc/nginx/conf.d/docs-search.ukfast.co.uk.conf
# COPY /nginx/docs.ukfast.co.uk.conf /etc/nginx/conf.d/docs.ukfast.co.uk.conf
# COPY /nginx/search.docs.devops.ukfast.co.uk.conf /etc/nginx/conf.d/search.docs.devops.ukfast.co.uk.conf