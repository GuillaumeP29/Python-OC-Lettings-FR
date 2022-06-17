FROM python:3.9-slim-buster
# -alpine  /  -slim-buster

WORKDIR /app

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH "/app"

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
# RUN sudo apt-get install libpq-dev python-dev
RUN python -m pip install -r requirements.txt

COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD python3 manage.py runserver 0.0.0.0:8000 essai

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
