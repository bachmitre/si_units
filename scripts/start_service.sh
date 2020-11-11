#!/bin/sh

# debug mode
if [ "$ENV" = "debug" ]; then
    python3 /app/service/main.py

# multiple workers
else
    if [ -z "$WORKERS" ]; then
        WORKERS=5
    fi

    export PYTHONPATH=/app/service
    exec gunicorn -k gthread wsgi:app \
        --name service \
        --bind 0.0.0.0:8000 \
        --workers $WORKERS \
        --log-level=info
fi
