FROM rsr-builder-image:1.0.0 AS builder
COPY generated /usr/src/app/generated
WORKDIR /usr/src/app/generated
RUN cargo build --release

FROM rsr-base-image:1.0.0
COPY --from=builder /usr/src/app/generated /usr/src/app/generated
WORKDIR /home/node/app/generated/dist
EXPOSE 8080
CMD [ "cargo","run", "--example", "server" ]
