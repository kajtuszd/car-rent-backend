FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /code
WORKDIR /code

COPY  . /code/

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
