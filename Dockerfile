FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "/app/manage.py", "-b", "0.0.0.0:8000"]
