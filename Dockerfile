FROM python:3.9-slim-buster

ENV POETRY_VERSION=1.1.13

# system dependencies
RUN apt-get update && apt-get install -y build-essential
RUN pip install "poetry==$POETRY_VERSION"

# copy requirements to cache in docker layer
RUN mkdir /opt/code
WORKDIR /opt/code

# Project initialization
COPY . .

# Install poetry to ensure Python dependencies are correct
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev
