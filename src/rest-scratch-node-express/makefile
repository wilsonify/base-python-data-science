
# function for creating version files with version string and date
ver_file = echo "1.0.0" > $(1) && date +%Y-%m-%d >> $(1)

.PHONY: all clean

all: clean dist/image-latest.zip

clean:
	rm -rf build
	rm -rf dist
	rm -rf generated/node_modules
	rm -f make-dag.png

build/VERSION.txt:
	mkdir -p build && $(call ver_file, $@)

dist/VERSION.txt:
	mkdir -p dist && $(call ver_file, $@)

build/docker-build-base.txt: build/VERSION.txt
	docker build -f Dockerfile-base -t rsne-base-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/base-latest.zip: dist/VERSION.txt build/docker-build-base.txt
	docker save rsne-base-image:latest -o $@

build/docker-build-builder.txt:  build/docker-build-base.txt
	docker build -f Dockerfile-builder -t rsne-builder-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/builder-latest.zip: dist/VERSION.txt build/docker-build-builder.txt
	docker save rsne-builder-image:latest -o $@

build/docker-build-image.txt: build/docker-build-builder.txt
	docker build -t rsne-image:latest --platform=amd64 . && $(call ver_file, $@)

dist/image-latest.zip: dist/VERSION.txt build/docker-build-image.txt
	docker save rsne-image:latest -o $@

make-dag.png:
	make -bnd | ~/repos/makefile2graph/make2graph | dot -Tpng -o $@

run: build/docker-build-image.txt
	docker run --rm --name rsne -p 49154:8080 rsne-image:latest