ARG base_image
FROM ${base_image}

# Install packages that we want to make available at build time
RUN apt-get update && apt-get install -y \
ca-certificates \
git \
jq \
wget \
build-essential \
gcc \
python3-dev \
python3-pip \
git \
zlib1g-dev

RUN pwd
COPY build-requirements.txt .
RUN pip3 install -r ./build-requirements.txt

# Set required CNB information
ARG stack_id
ENV CNB_STACK_ID=${stack_id}
LABEL io.buildpacks.stack.id=${stack_id}

# Set user and group (as declared in base image)
USER ${CNB_USER_ID}:${CNB_GROUP_ID}