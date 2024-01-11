FROM python:3.10

RUN set -eux \
 && pip3 install django==3.2

CMD [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
