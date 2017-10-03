FROM node:6
RUN npm install -g phantomjs@2.1.7
ADD . /app
WORKDIR /app
CMD ["/app/tests.sh"]
