FROM mhart/alpine-node:8
# RUN mkdir /wof
# ADD . /wof
# RUN cd /wof
# RUN npm install
WORKDIR /wof
COPY package.json .
RUN npm install
COPY . .