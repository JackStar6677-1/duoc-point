.PHONY: up down migrate createsuperuser test

up:
	docker compose up -d

down:
	docker compose down

migrate:
	docker compose run --rm django python manage.py migrate

createsuperuser:
	docker compose run --rm django python manage.py createsuperuser

test:
	docker compose run --rm django pytest
