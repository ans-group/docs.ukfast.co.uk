FROM python:3.8-alpine3.13 as builder

RUN pip install Sphinx recommonmark
RUN apk add build-base

WORKDIR /build/

ADD Makefile rasterize.js tests.sh /build/
ADD ./files/ ./files/
ADD ./source/ ./source/

RUN make clean && \
    sphinx-build -n -b dirhtml -d build/doctrees source/ build/html && \
    make build/html/_static/css/app.css && \
    make build/html/_static/app.js


FROM nginx:stable
ARG essvc=elasticsearch

RUN apt update
RUN apt install curl -y

COPY --from=builder /build/build/html /usr/share/nginx/docs.ukfast.co.uk/html/docs

COPY /nginx/nginx.conf /etc/nginx/nginx.conf

RUN sed -i "s/elasticsearch/$essvc/" /etc/nginx/nginx.conf

