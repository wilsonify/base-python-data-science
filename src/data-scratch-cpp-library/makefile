
all: clean build_dir cmake make

clean:
	rm -rf build

build_dir:
	mkdir -p build

cmake: build_dir
	cd build && cmake ..

make: cmake
	cd build && make all