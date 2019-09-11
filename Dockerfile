FROM python:2-alpine as builder

RUN pip install Sphinx===1.6.6 recommonmark==0.4.0 sphinxcontrib.youtube
RUN apk add build-base

WORKDIR /build/

ADD Makefile rasterize.js tests.sh /build/
ADD ./files/ ./files/
ADD ./ukf/ ./ukf/
# Do two copies, the above wont change much, adds a layer but saves time
ADD ./source/ ./source/

RUN make clean && \
    sphinx-build -nW -b html -d build/doctrees source/ build/html && \
    make build/html/_static/css/app.css && \
    make build/html/_static/app.js

FROM nginx:stable

COPY --from=builder /build/build/html /usr/share/nginx/html

