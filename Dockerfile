FROM python/3.12.7-alpine3.20

ENV status=dev

RUN adduser -D -s /bin/sh wolf
WORKDIR /home/wolf

ADD entrypoint.sh entrypoint.sh
RUN chmod 755 entrypoint.sh && chown wolf:wolf entrypoint.sh
USER wolf

ADD wolf.py /home/wolf/wolf.py

ENTRYPOINT ["./entrypoint.sh"]
