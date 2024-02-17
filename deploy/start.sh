#! /usr/bin/env bash
set -e

# Start Granian 
# https://github.com/emmett-framework/granian
# exec granian --interface asgi "$GRANIAN_INTERFACE" "$APP_MODULE"

PORT=${PORT:-80}
HOST=${HOST:-"0.0.0.0"}
WORKERS=${WORKERS:-1}
THREADS=${THREADS:-1}

exec granian --interface asgi --port $PORT --host $HOST --workers $WORKERS --threads $THREADS main:app
