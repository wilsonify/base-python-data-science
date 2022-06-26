FROM python:3-alpine as builder
RUN apk update && apk upgrade && apk add \
binutils \
gcc \
musl-dev \
python3-dev \
git
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r build-requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 setup-maximal.py install
RUN apk add binutils
RUN pyinstaller \
--noconfirm \
--onedir \
--console \
--distpath dist \
--workpath build \
--specpath . \
data_science_from_scratch/__main__.py

FROM alpine:3.16.0
RUN mkdir -p /app
COPY --from=builder /usr/src/app/dist/__main__ /app
WORKDIR /app
ENV AMQP_HOST=localhost
ENV AMQP_PORT=5672
ENV AMQP_ROUTING_KEY="dsfs"
ENV AMQP_HEARTBEAT=10000
ENV AMQP_TIMEOUT=10001
ENV AMQP_USER="guest"
ENV AMQP_PASS="guest"
ENTRYPOINT ["/app/__main__"]
