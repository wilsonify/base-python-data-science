FROM python:3-alpine as builder
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r build-requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
RUN apk add binutils
RUN pyinstaller \
--noconfirm \
--onedir \
--console \
--distpath dist \
--workpath build \
--specpath . \
data_science_from_scratch/__main__.py

FROM alpine:3.16.0
RUN mkdir -p /app
COPY --from=builder /usr/src/app/dist/__main__ /app
WORKDIR /app
ENTRYPOINT ["/app/__main__"]
