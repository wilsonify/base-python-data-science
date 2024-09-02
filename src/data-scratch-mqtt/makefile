# function for creating version files with version string and date
ver_file = echo "1.0.0" > $(1) && date +%Y-%m-%d >> $(1)

all: data-scratch-mqtt

build/VERSION.txt:
	mkdir -p build && $(call ver_file, $@)

build/base.txt: build/VERSION.txt
	docker build -f Dockerfile-base -t data-scratch-mqtt-base:1.0.0 . && $(call ver_file, $@)

build/builder.txt: build/base.txt
	docker build -f Dockerfile-builder -t data-scratch-mqtt-builder:1.0.0 . && $(call ver_file, $@)

build/image.txt: build/builder.txt
	docker build -f Dockerfile -t data-scratch-mqtt:1.0.0 . && $(call ver_file, $@)

stop:
	docker stop data-scratch-mqtt | true

run: stop
	docker run --rm --name data-scratch-mqtt -d --network host data-scratch-mqtt:1.0.0