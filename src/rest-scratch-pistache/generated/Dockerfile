FROM rest-scratch-pistache-builder:1.0.0 AS builder
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN make all
RUN ldd build/api-server

FROM rest-scratch-pistache-base:1.0.0
COPY --from=builder /usr/src/app/dist /usr/src/app/dist
WORKDIR /usr/src/app/dist
EXPOSE 8080
ENTRYPOINT [ "./api-server" ]
