FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Port to expose
EXPOSE 8000

# start flask
CMD ["/bin/sh", "/app/scripts/start_service.sh"]
