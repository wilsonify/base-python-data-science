ARG base_image
FROM ${base_image}

# Set required CNB information
ARG stack_id
LABEL io.buildpacks.stack.id="${stack_id}"

USER root
RUN mkdir -p /app && chown ${CNB_USER_NAME} /app && chgrp ${CNB_USER_NAME} /app 

# Set user and group (as declared in base image)
USER ${CNB_USER_ID}:${CNB_GROUP_ID}