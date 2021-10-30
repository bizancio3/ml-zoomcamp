FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["app.py", "water1.bin", "./"]

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000", "app:app"]