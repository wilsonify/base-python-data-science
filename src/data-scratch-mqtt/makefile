
all: data-scratch-mqtt

data-scratch-mqtt-base:
	docker build -f Dockerfile-base -t data-scratch-mqtt-base:latest .

data-scratch-mqtt-builder: data-scratch-mqtt-base
	docker build -f Dockerfile-builder -t data-scratch-mqtt-builder:latest .

data-scratch-mqtt: data-scratch-mqtt-builder
	docker build -f Dockerfile -t data-scratch-mqtt:latest .

stop:
	docker stop data-scratch-mqtt | true

run: stop
	docker run --rm --name data-scratch-mqtt -d --network host data-scratch-mqtt:latest