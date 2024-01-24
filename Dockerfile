FROM python:3.10

RUN set -eux \
 && pip3 install django==3.2

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "introduced_facility.wsgi:application" ]
