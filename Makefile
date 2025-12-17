.PHONY: help start stop restart logs

help:
	@echo "make start    - Start containers"
	@echo "make stop     - Stop containers"
	@echo "make restart  - Restart containers"
	@echo "make logs     - Show logs"

start:
	docker compose up --build -d

stop:
	docker compose down

restart:
	docker compose down && docker compose up --build -d

logs:
	docker compose logs -f
