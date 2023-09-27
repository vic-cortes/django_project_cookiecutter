FROM python:{{ cookiecutter.python_version }}-slim-bullseye as base

# set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_NO_INPUT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    VENV_PATH=/opt/venv \
    APP_PATH=/opt/{{ cookiecutter.project_slug }}

ENV PATH=$VENV_PATH/bin:$PATH

RUN python -m venv ${VENV_PATH} \
    && pip install -U pip wheel poetry

WORKDIR ${APP_PATH}

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

from base as builder

# Uncomment these lines if you need to install OS dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     g++ \
#     && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

RUN poetry install --without dev --sync

FROM base as development

ENV PYTHONDONTWRITEBYTECODE=1

COPY --from=builder ${VENV_PATH} ${VENV_PATH}

RUN poetry install --with dev --sync

FROM base as release

COPY --from=builder ${VENV_PATH} ${VENV_PATH}

COPY . ${APP_PATH}

ENTRYPOINT ["./entrypoints/run_gunicorn.sh"]
