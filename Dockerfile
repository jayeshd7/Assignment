# pull official base image
FROM ubuntu:22.04

# set work directory
WORKDIR /assignment

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file

COPY ./requirements.txt /assignment/requirements.txt

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc git libssl-dev g++ make python3-dev python3-pip \
   # && pip3 install --upgrade pip3 setuptools wheel \
    && pip3 install -r /assignment/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY app/ /assignment/app
RUN ls -latr /assignment

# execute command
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]