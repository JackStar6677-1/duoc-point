#!/usr/bin/env bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r server/requirements.txt

# Apply migrations and run server
python server/manage.py migrate --noinput
python server/manage.py runserver 0.0.0.0:8000
