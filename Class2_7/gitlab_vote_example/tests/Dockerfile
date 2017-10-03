FROM node:6
RUN npm install -g phantomjs
ADD . /app
WORKDIR /app
CMD ["/app/tests.sh"]
