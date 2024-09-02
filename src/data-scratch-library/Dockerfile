FROM data-scratch-library-builder:1.0.0 AS builder
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 setup-maximal.py bdist
