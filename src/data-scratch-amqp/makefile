
all: data-scratch-amqp

data-scratch-amqp-base:
	docker build -f Dockerfile-base -t data-scratch-amqp-base:1.0.0 .

data-scratch-amqp-builder: data-scratch-amqp-base
	docker build -f Dockerfile-builder -t data-scratch-amqp-builder:1.0.0 .

data-scratch-amqp: data-scratch-amqp-builder
	docker build -f Dockerfile -t data-scratch-amqp:1.0.0 .

stop:
	docker stop data-scratch-amqp | true

run: stop
	docker run --rm --name data-scratch-amqp --network host data-scratch-amqp:1.0.0