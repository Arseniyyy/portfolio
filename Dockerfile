FROM python:3

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN touch debug.log

RUN touch db.sqlite3

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD gunicorn -c gunicorn_config.py --log-level debug portfolio.wsgi:application --bind 0.0.0.0:$PORT