FROM python:3.10

WORKDIR /app

RUN set -eux \
 && pip3 install django==3.2 gunicorn==21.2

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "introduced_facility.wsgi:application" ]
