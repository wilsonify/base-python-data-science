FROM rsne-builder-image:latest as builder
COPY generated /usr/src/app/generated
WORKDIR /usr/src/app/generated
RUN npm install

FROM rsne-base-image:latest
COPY --from=builder /usr/src/app/generated/node_modules /usr/src/app/generated/node_modules
COPY --from=builder /usr/src/app/generated /usr/src/app/generated
WORKDIR /usr/src/app/generated
EXPOSE 8080
CMD ["node", "index.js" ]