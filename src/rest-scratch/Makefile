# Makefile for creating our standalone Cython program
MODULE := openapi_server
PYTHON := python3
CYTHON := cython
PYVERSION := $(shell $(PYTHON) -c "import sys; print(sys.version[:3])")
PYPREFIX := $(shell $(PYTHON) -c "import sys; print(sys.prefix)")
INCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
PLATINCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc(plat_specific=True))")
LIBDIR1 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
LIBDIR2 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBPL'))")
PYLIB := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")
CC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('CC'))")
LINKCC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKCC'))")
LINKFORSHARED := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKFORSHARED'))")
LIBS := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBS'))")
SYSLIBS :=  $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('SYSLIBS'))")

.PHONY: paths all clean test

paths:
	@echo "PYTHON=$(PYTHON)"
	@echo "MODULE=$(MODULE)"
	@echo "CYTHON=$(CYTHON)"
	@echo "PYVERSION=$(PYVERSION)"
	@echo "PYPREFIX=$(PYPREFIX)"
	@echo "INCDIR=$(INCDIR)"
	@echo "PLATINCDIR=$(PLATINCDIR)"
	@echo "LIBDIR1=$(LIBDIR1)"
	@echo "LIBDIR2=$(LIBDIR2)"
	@echo "PYLIB=$(PYLIB)"
	@echo "CC=$(CC)"
	@echo "LINKCC=$(LINKCC)"
	@echo "LINKFORSHARED=$(LINKFORSHARED)"
	@echo "LIBS=$(LIBS)"
	@echo "SYSLIBS=$(SYSLIBS)"

$(MODULE).out: $(MODULE).o
	$(LINKCC) -o $@ $^ -L$(LIBDIR1) -L$(LIBDIR2) -l$(PYLIB) $(LIBS) $(SYSLIBS) $(LINKFORSHARED)

$(MODULE).o: $(MODULE).c
	$(CC) -c -fPIC $^ -I$(INCDIR) -I$(PLATINCDIR) -o $@

$(MODULE).c: $(MODULE).py
	@$(PYTHON) -m $(CYTHON) -3 --embed $^

all: $(MODULE).out

clean:
	@echo Cleaning ~ files
	@rm -rf **/*~
	@rm -rf *~
	@echo Cleaning .o files
	@rm -rf **/*.o
	@rm -rf *.o
	@echo Cleaning .so files
	@rm -rf **/*.so
	@rm -rf *.so
	@echo Cleaning .c files
	@rm -rf **/*.c
	@rm -rf *.c
	@echo Cleaning .out files
	@rm -rf *.out
	@echo Cleaning build
	@rm -rf build
	@echo Cleaning dist
	@rm -rf dist
	@echo Cleaning .egg-info
	@rm -rf *.egg-info

test: clean all
	LD_LIBRARY_PATH=$(LIBDIR1):$$LD_LIBRARY_PATH ./$(MODULE) > test.output
	$(PYTHON) assert_equal.py MODULE.output test.output

docker-build:
	docker build -t rest-scratch .

docker-run:
	docker run --rm -p 49153:8080 --name rest-scratch rest-scratch

__main__.spec:
	pyinstaller --noconfirm --onedir --console --distpath dist --workpath build --specpath . --add-data openapi_server/openapi:openapi --collect-all "connexion" openapi_server/__main__.py

dist/__main__:
	pyinstaller --noconfirm --onedir --console --distpath dist --workpath build --specpath . --add-data openapi_server/openapi:openapi openapi_server/__main__.spec
