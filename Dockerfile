FROM node:slim AS base

RUN apt update -y && apt install git -y

# install hexo
RUN npm set registry https://registry.npm.taobao.org && \
    npm install -g hexo-cli

FROM base AS hexo-config
CMD bash ./init-hexo-config.sh

FROM base AS hexo-box
CMD bash
