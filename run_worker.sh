#!/usr/bin/env bash

/bin/bash scripts/wait-for-it.sh redis:6379

export PYTHONPATH=src

celery worker -A app.celery -b "$CELERY_BROKER_URL" --result-backend "$CELERY_RESULT_BACKEND" --loglevel=debug
