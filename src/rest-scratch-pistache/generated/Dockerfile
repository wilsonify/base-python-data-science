FROM rest-scratch-pistache-builder:latest as builder
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN make all

FROM rest-scratch-pistache-base:latest
COPY --from=build /usr/src/app/dist /usr/src/app
WORKDIR /usr/src/app
ENTRYPOINT [ "api-server" ]
