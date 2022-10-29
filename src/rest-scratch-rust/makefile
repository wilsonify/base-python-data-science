
# function for creating version files with version string and date
ver_file = echo "1.0.0" > $(1) && date +%Y-%m-%d >> $(1)

.PHONY: all clean

all: clean dist/image-latest.tar

clean:
	rm -rf build
	rm -rf dist
	rm -rf generated/node_modules
	rm -rf generated/dist
	rm -f make-dag.png

build/VERSION.txt:
	mkdir -p build && $(call ver_file, $@)

dist/VERSION.txt:
	mkdir -p dist && $(call ver_file, $@)

generated/node_modules/VERSION.txt:
	cd generated && npm install && cd .. && $(call ver_file, $@)

dist/index.js: generated/node_modules/VERSION.txt
	cd generated && npx webpack

generated/dist/api/openapi.yaml:
	mkdir -p generated/dist/api && cp generated/api/openapi.yaml generated/dist/api/openapi.yaml

generated/dist/node_modules/VERSION.txt:
	mkdir -p generated/dist/node_modules && cp -R generated/node_modules generated/dist

start: dist/index.js generated/dist/api/openapi.yaml generated/dist/node_modules/VERSION.txt
	cd generated && node dist/index.js

build/docker-build-base.txt: build/VERSION.txt
	docker build -f Dockerfile-base -t rsr-base-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/base-latest.tar: dist/VERSION.txt build/docker-build-base.txt
	docker save rsr-base-image:latest -o $@

build/docker-build-builder.txt:  build/docker-build-base.txt
	docker build -f Dockerfile-builder -t rsr-builder-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/builder-latest.tar: dist/VERSION.txt build/docker-build-builder.txt
	docker save rsr-builder-image:latest -o $@

build/docker-build-image.txt: build/docker-build-builder.txt
	docker build -t rsr-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/image-latest.tar: dist/VERSION.txt build/docker-build-image.txt
	docker save rsr-image:latest -o $@

image-latest.tar: dist/image-latest.tar

make-dag.png:
	make -bnd | ~/repos/makefile2graph/make2graph | dot -Tpng -o $@

docker-stop:
	docker stop rsr || true

docker-run: build/docker-build-image.txt docker-stop
	# Node.js was not designed to run as PID 1, --init wraps Node.js with tini
	docker run --rm \
--name rsr \
-p 49154:8080 \
rsr-image:latest

