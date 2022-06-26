FROM python:3-alpine as builder
RUN apk update && apk upgrade
RUN apk add \
binutils \
gcc \
musl-dev \
python3-dev \
git

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN ls
RUN pip3 install -r build-requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 setup.py install

RUN pyinstaller \
--noconfirm \
--onedir \
--console \
--distpath dist \
--workpath build \
--specpath . \
--add-data openapi_server/openapi:openapi \
--collect-all "connexion" \
--collect-all "swagger_ui_bundle" \
--collect-all "openapi_spec_validator" \
openapi_server/__main__.py

FROM alpine:3.16.0
RUN mkdir -p /app
COPY --from=builder /usr/src/app/dist/__main__ /app
WORKDIR /app
EXPOSE 8080
ENV AMQP_HOST=localhost
ENV AMQP_PORT=5672
ENV DSFS_AMQP_ROUTING_KEY="dsfs"
ENV AMQP_HEARTBEAT=10000
ENV AMQP_TIMEOUT=10001
ENV AMQP_USER="guest"
ENV AMQP_PASS="guest"
ENTRYPOINT ["/app/__main__"]
