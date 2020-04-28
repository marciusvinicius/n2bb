FROM python:3.8.0-slim

MAINTAINER Marcius Oliveira "marciusoliveiraa@gmail.com"

WORKDIR /usr/src/app
COPY ./requirements.txt .

# Dependencies
RUN set -ex; \
    update-ca-certificates; \
    apt update; \
    apt install --no-install-recommends -y gcc python3-dev default-libmysqlclient-dev python3-psycopg2 wkhtmltopdf; \
    pip install --no-cache-dir --upgrade setuptools pip; \
    pip install --no-cache-dir -r requirements.txt; \
    apt remove -y gcc python3-dev; apt autoremove -y; apt autoclean -y; \
    rm -rf /var/lib/apt/lists/*;

COPY . .
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "--threads", "2", "--reload", "wsgi"]
