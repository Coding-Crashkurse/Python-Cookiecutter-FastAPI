FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

{%- if cookiecutter.frontend == "vue" -%}
# Ich bin vue Content

{%- elif cookiecutter.license == "react" -%}
# Ich bin react Content

{% endif %}


COPY . .

EXPOSE {{cookiecutter.port}}