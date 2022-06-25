
all: docker-build	

docker-build:
	docker build -t dsfs .

docker-run: docker-build
	docker run --rm --name dsfs --env AMQP_HOST=thinkpad dsfs
