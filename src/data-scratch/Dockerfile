FROM python:3-alpine as builder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apk add binutils

RUN pip3 install pyinstaller
RUN find . -name "*.pyc" -exec rm {} \;
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python setup.py bdist_wheel
RUN python -m compileall data_science_from_scratch
RUN pyinstaller data_science_from_scratch/__main__.py \
--distpath dist \
--workpath build \
--noconfirm \
--clean \
--log-level DEBUG \
--onedir \
--name data_science_from_scratch 
RUN find . -name "*.py" -exec rm {} \;
ENTRYPOINT ["/bin/sh"]

#FROM python:3-alpine
#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app
#COPY --from builder /usr/src/app/dist/data_science_from_scratch-0.0.0-py3-none-any.whl /usr/src/app
#RUN pip3 install --no-cache-dir -r requirements.txt
#RUN pip install data_science_from_scratch-0.0.0-py3-none-any.whl
#EXPOSE 8080
#ENTRYPOINT ["python3"]
#CMD ["-m", "data_science_from_scratch"]