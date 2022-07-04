FROM alpine:3.16

ARG cnb_user="cnb"
ARG cnb_uid=1000
ARG cnb_gid=1001

# Install packages that we want to make available at both build and run time
RUN set -eux && apk add --update --no-cache ca-certificates tzdata

# Create user and group
RUN addgroup -g ${cnb_gid} ${cnb_user} && adduser -u ${cnb_uid} -G ${cnb_user} -s /bin/bash -D ${cnb_user}

# Set required CNB information
ENV CNB_USER_NAME=${cnb_user}
ENV CNB_USER_ID=${cnb_uid}
ENV CNB_GROUP_ID=${cnb_gid}
