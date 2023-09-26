.DEFAULT_GOAL:=help
SHELL:=/bin/bash

include .env

app:
	@echo "Creating app..."
	mkdir {{ cookiecutter.project_slug }}/${app_name}
	python manage.py startapp ${app_name} {{ cookiecutter.project_slug }}/${app_name}