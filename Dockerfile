FROM python:3.6
LABEL maintainer="tibor.kiss@gmail.com"

RUN mkdir /build

ENV TWS_API twsapi_macunix.973.05.zip
ADD http://interactivebrokers.github.io/downloads/${TWS_API} /build/
RUN python -m zipfile -e /build/${TWS_API} /build/tws_api && \
    cd /build/tws_api/IBJts/source/pythonclient && \
    python setup.py install

ADD . /build/ib_dl
WORKDIR /build/ib_dl
RUN python setup.py install

ENTRYPOINT ["/usr/local/bin/ib-dl"]
