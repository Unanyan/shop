FROM python:3.6.6-alpine3.7

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true
#   PIPENV_DOTENV_LOCATION=config/.env


# System deps:

RUN apk --no-cache add \
     bash \
     build-base \
     curl \
     gcc \
     gettext \
     git \
     libffi-dev \
     linux-headers \
     musl-dev \
     postgresql-client \
     postgresql-dev \
     tini \
     build-base \
     jpeg-dev \
     zlib-dev

# Creating folders, and files for a project:

COPY . /code
WORKDIR /code

# Project initialization:

#RUN chmod +x "/docker-entrypoint.sh" \
RUN pip install pipenv \
  && pipenv install --deploy --system --ignore-pipfile

ENTRYPOINT ["/sbin/tini", "--"]

VOLUME /app/shop/media
