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

# Load environment variables for local dev
if [ -f infra/.env.example ] && [ ! -f infra/.env ]; then
  cp infra/.env.example infra/.env
fi
set -o allexport
if [ -f infra/.env ]; then
  source infra/.env
fi
set +o allexport

# Enable demo mode for exploring APIs without auth
export DEMO_MODE=1

# Apply migrations and create default admin user
python server/manage.py migrate --noinput
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin123
export DJANGO_SUPERUSER_EMAIL=admin@example.com
python server/manage.py createsuperuser --noinput >/dev/null 2>&1 || true

# Run server
python server/manage.py runserver 0.0.0.0:8000
