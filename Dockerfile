FROM python:3.9.13-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip3 install --user -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000