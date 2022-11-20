FROM data-scratch-mqtt-builder:latest as builder
USER root
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install .
RUN pyinstaller \
--noconfirm \
--onedir \
--console \
--distpath dist \
--workpath build \
--specpath . \
data_scratch_mqtt/__main__.py

FROM data-scratch-mqtt-base:latest
COPY --from=builder /usr/src/app/dist/__main__ /app
WORKDIR /app
ENV MQTT_HOST=localhost
ENV MQTT_PORT=5672
ENV MQTT_ROUTING_KEY="dsfs"
ENV MQTT_HEARTBEAT=10000
ENV MQTT_TIMEOUT=10001
ENV MQTT_USER="thom"
ENV MQTT_PASS="guest"
ENTRYPOINT ["/app/__main__"]
#ENTRYPOINT ["python3", "-m", "data_scratch_mqtt"]