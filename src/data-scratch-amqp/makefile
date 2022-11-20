
all: data-scratch-amqp

data-scratch-amqp-base:
	docker build -f Dockerfile-base -t data-scratch-amqp-base:latest .

data-scratch-amqp-builder: data-scratch-amqp-base
	docker build -f Dockerfile-builder -t data-scratch-amqp-builder:latest .

data-scratch-amqp: data-scratch-amqp-builder
	docker build -f Dockerfile -t data-scratch-amqp:latest .

stop:
	docker stop data-scratch-amqp | true

run: stop
	docker run --rm --name data-scratch-amqp --network host data-scratch-amqp:latest