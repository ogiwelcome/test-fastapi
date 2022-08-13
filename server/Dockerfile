FROM python:3.9.13

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--reload"]
