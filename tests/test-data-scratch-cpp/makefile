ver_file = echo "1.0.0" > $(1) && date +%Y-%m-%d >> $(1)

all: clean build/test-data-scratch-cpp

build/version.txt:
	mkdir -p build && $(call ver_file, $@)

dist/version.txt:
	mkdir -p dist && $(call ver_file, $@)

external/googletest/googletest/include/gtest/gtest.h:
	git submodule update --init --recursive

gtest: external/googletest/googletest/include/gtest/gtest.h

clean:
	rm -rf build
	rm -rf dist

build/Makefile: build/version.txt gtest
	cd build && cmake .. -G Ninja

build/test-data-scratch-cpp:  build/Makefile
	cd build && ninja 

build/Testing/Temporary/LastTest.log:
	cd build && ctest 

test: build/Testing/Temporary/LastTest.log
	
build/base-python-data-science-1.0.1-Linux.tar.gz:
	cd build && cpack

dist/base-python-data-science-1.0.1-Linux.tar.gz: dist/version.txt build/base-python-data-science-1.0.1-Linux.tar.gz
	# move dependencies of the current rule
	cp -rf $^ dist

build/base-python-data-science-base.txt: build/version.txt
	docker build -t base-python-data-science-base -f Dockerfile-base . && $(call ver_file, $@)

build/base-python-data-science-builder.txt: build/base-python-data-science-base.txt
	docker build -t base-python-data-science-builder -f Dockerfile-builder . && $(call ver_file, $@)

build/base-python-data-science-image.txt: build/base-python-data-science-builder.txt
	docker build -t base-python-data-science -f Dockerfile . && $(call ver_file, $@)

docker-run: build/base-python-data-science-image.txt
	docker run --rm --name base-python-data-science base-python-data-science:latest

docker/build/test-data-scratch-cpp: build/base-python-data-science-builder.txt
	docker run --rm --name base-python-data-science-builder -u 1000:1000 -v $(shell pwd):/usr/src/app base-python-data-science-builder:latest make all