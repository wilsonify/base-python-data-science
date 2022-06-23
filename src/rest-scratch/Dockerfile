FROM python:3-alpine as builder
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r build-requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 setup-minimal.py install
RUN apk add binutils
RUN pyinstaller --noconfirm --onedir --console --distpath dist --workpath build --specpath . --add-data openapi_server/openapi:openapi --collect-all "connexion" --collect-all "openapi_server" openapi_server/__main__.py
ENTRYPOINT ["/usr/src/app/dist/__main__/__main__"]

#FROM python:3-alpine
#RUN mkdir -p /usr/src/app
#COPY --from=builder dist /usr/src/app
#WORKDIR /usr/src/app/__main__
#RUN pip3 install --no-cache-dir -r requirements.txt
#EXPOSE 8080
#ENTRYPOINT ["/usr/src/app/__main__/__main__"]
