FROM python:3.10 AS django

RUN set -eux \
 && pip3 install django==3.2

FROM nginx:1.25.3

COPY --from=django /usr/local/lib/python3.10/site-packages/django/contrib/admin/static/admin /app_admin/static/admin
