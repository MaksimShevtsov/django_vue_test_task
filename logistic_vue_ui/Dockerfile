FROM node:16.15.0

ARG PROG_DIR=/vue_proj

RUN mkdir -p ${PROG_DIR}
COPY ./logistic_vue_ui ${PROG_DIR}

WORKDIR ${PROG_DIR}

RUN npm install -g @vue/cli

COPY ./logistic_vue_ui/package.json ${PROG_DIR}
COPY ./logistic_vue_ui/package-lock.json ${PROG_DIR}

RUN npm install

CMD ["npm", "run", "serve"]