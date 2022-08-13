FROM python:3.9.13

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--reload"]
