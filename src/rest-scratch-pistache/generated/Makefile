ver_file = echo "1.0.0" > $(1) && date +%Y-%m-%d >> $(1)

all: clean dist/api-server

clean:
	rm -rf build
	rm -rf dist	

build/VERSION.txt:
	mkdir -p build && $(call ver_file, $@)

dist/VERSION.txt:
	mkdir -p dist && $(call ver_file, $@)

external/googletest/CMakeLists.txt:
	git submodule update --init --recursive 

build/makefile: build/VERSION.txt external/googletest/CMakeLists.txt
	cd build && cmake .. -G Ninja

build/api-server: build/makefile
	cd build && ninja

dist/api-server: dist/VERSION.txt build/api-server
	cp build/api-server dist

build/rest-scratch-pistache-base.txt: build/VERSION.txt
	docker build -f Dockerfile-base -t rest-scratch-pistache-base:latest . && $(call ver_file, $@)

build/rest-scratch-pistache-builder.txt:  build/rest-scratch-pistache-base.txt
	docker build -f Dockerfile-builder -t rest-scratch-pistache-builder:latest . && $(call ver_file, $@)

build/rest-scratch-pistache.txt: build/rest-scratch-pistache-builder.txt
	docker build -t rest-scratch-pistache:latest . && $(call ver_file, $@)

docker-run: build/rest-scratch-pistache.txt
	docker run --rm --name rest-scratch-pistache -p 49153:8080 rest-scratch-pistache:latest
