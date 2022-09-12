FROM rsne-builder-image:latest as builder
COPY generated /usr/src/app/generated
WORKDIR /usr/src/app/generated
RUN npm install
RUN npx webpack

FROM rsne-base-image:latest
COPY --from=builder /usr/src/app/generated/dist /usr/src/app/generated/dist
WORKDIR /usr/src/app/generated/dist
EXPOSE 8080
CMD ["node", "main.js" ]
