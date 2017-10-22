FROM ruby:2.4.1-alpine
ADD ./ /app/
WORKDIR /app
ENV PORT 5000
EXPOSE 5000

CMD ["sh", "-c", "while :; do ruby ./server.rb; done"]
