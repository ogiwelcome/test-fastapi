FROM python:3.9.13

ADD ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--reload"]
