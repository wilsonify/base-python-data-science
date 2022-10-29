FROM rsne-builder-image:latest as builder
COPY generated /home/node/app/generated
WORKDIR /home/node/app/generated
RUN npx webpack

FROM rsne-base-image:latest
COPY --from=builder /home/node/app/generated /home/node/app/generated
COPY --from=builder /home/node/app/generated/api /home/node/app/generated/dist/api
WORKDIR /home/node/app/generated/dist
EXPOSE 8080
CMD ["node", "index.js" ]
