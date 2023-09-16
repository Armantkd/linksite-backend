FROM python:latest

# Install pip
RUN python -m ensurepip --upgrade

# USER app
ENV PYTHONUNBUFFERED 1

#setup
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/