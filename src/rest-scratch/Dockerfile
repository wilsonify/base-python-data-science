FROM python:3-alpine as builder
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r build-requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 setup-minimal.py develop
RUN apk add binutils
RUN pyinstaller \
--noconfirm \
--onedir \
--console \
--distpath dist \
--workpath build \
--specpath . \
--add-data openapi_server/openapi:openapi \
--collect-all "connexion" \
--collect-all "swagger_ui_bundle" \
openapi_server/__main__.py

FROM alpine:3.16.0
RUN mkdir -p /app
COPY --from=builder /usr/src/app/dist/__main__ /app
#/lib/ld-musl-x86_64.so.1
#/lib/libz.so.1
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["/app/__main__"]
