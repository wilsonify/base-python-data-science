
clean:
	rm -rf build
	rm -rf dist
	rm dsl/*.c

data-scratch-library-base:
	docker build -t data-scratch-library-base:1.0.0 -f Dockerfile-base .

data-scratch-library-builder: data-scratch-library-base
	docker build -t data-scratch-library-builder:1.0.0 -f Dockerfile-builder .

dist/dsl-1.0.0.linux-x86_64.whl: data-scratch-library-builder
	docker run --rm -u 1000:1000 -v "$(PWD):/usr/src/app" data-scratch-library-builder:1.0.0 python3 setup-maximal.py bdist_wheel

wheel: dist/dsl-1.0.0.linux-x86_64.whl

docker-build:
	docker build -t dsfs .

docker-run: docker-build
	docker run --rm --name dsfs --env AMQP_HOST=thinkpad dsfs

dsl.so:
	pyinstaller