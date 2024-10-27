FROM golang:1.23.2-alpine3.20

ENV status=dev

RUN adduser -D -s /bin/sh wolf
WORKDIR /home/wolf

ADD entrypoint.sh entrypoint.sh
RUN chmod 755 entrypoint.sh && chown wolf:wolf entrypoint.sh
USER wolf

ADD wolf.go /home/wolf/wolf.go

RUN go build wolf.go

ENTRYPOINT ["./entrypoint.sh"]
