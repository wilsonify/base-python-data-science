FROM data-scratch-library-builder:latest as builder
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 setup-maximal.py bdist
