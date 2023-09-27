.DEFAULT_GOAL:=help
SHELL:=/bin/bash

include .env

create_app:
	@echo "Creating app..."
	mkdir {{ cookiecutter.project_slug }}/${app_name}
	python manage.py startapp ${app_name} {{ cookiecutter.project_slug }}/${app_name}

run_dev_server:
	python manage.py runserver --settings=config.settings.local


help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.env:
	cp env-sample .env;

build: .env  ## Builds the docker images
	docker-compose build

rebuild: .env  ## Rebuilds the docker images to add any updates in the build
	docker-compose build --no-cache

start: .env  ## Start the server on http://localhost:8000
	docker compose up -d

stop:  ## Stop all project docker containers
	docker compose down

shell: .env  ## Run a shell, like SSH-ing into the docker machine
	docker compose run --rm --entrypoint "/bin/bash" web

django_shell: .env  ## Run a Django shell
	docker compose run --rm --entrypoint "bash -c 'cd source && python manage.py shell_plus'" web

migrations: .env  ## Generate migration files
	docker compose run --rm --entrypoint "./source/manage.py makemigrations" web

migrate: .env  ## Apply migrations to database
	docker compose run --rm --entrypoint "./source/manage.py migrate" web

superuser: .env  ## Create a superuser account
	docker compose run --rm --entrypoint "./source/manage.py createsuperuser" web
