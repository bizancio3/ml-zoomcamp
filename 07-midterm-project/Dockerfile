FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "water1.bin", "./"]

EXPOSE 8000

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]