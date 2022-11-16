# Python Student Service

This service stores Students and is an example of an architecture for a python fastapi micro-service.

## Setup

### Python Environment

- [Python 3.10](https://www.python.org/downloads/)
- [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

### Docker

#### Building Database image

```bash
cd docker/postgres
docker build --tag motimatic-postgres .
```

#### Starting db and updating to latest migration

```bash
make db  # db runs on port 5433 -> 5432 on docker
```

#### Building motimatic-student-svc base image

```bash
# from project-root
docker build --tag motimatic-student-base -f base.Dockerfile .
```

#### Login to Snyk

> Only needed if you plan on running Snyk locally, right now CI handles Snyk scans

1. Install [Snyk](https://snyk.io/docs/cli-installation/)

1. Sign up for a Snyk account [here](https://app.snyk.io/signup)

1. Authenticate using your account
   ```bash
   snyk auth
   ```

### Migrations

#### Upgrading/Downgrading

```bash
make db # upgrade to the lastest revision
pipenv run alembic upgrade head # Upgrade to the most recent
pipenv run alembic upgrade +1 # Upgrade one migration
pipenv run alembic downgrade -2 # Downgrade two migrations
pipenv run alembic upgrade ae1027a6acf+2 # Upgrade to ae1027a6acf and two addition migrations forward
```

#### Generating new migrations automatically based on model changes

- Update appropriate models in `app/models`
- Run `pipenv run alembic revision --autogenerate -m "migration name here"`
- Edit the generated migration file
  - NOTE: the generated migration may be missing imports or may have extraneous values added. As a result, the migration may not be executable immediately after generation
- Test migration via `make db`

#### Generating new migrations manually

- Run `pipenv run alembic revision -m "migration name here"`
- Edit the generated migration file
- Test migration via `pipenv run alembic upgrade head`

## Starting, Testing, etc

A `Makefile` contains useful commands

### Starting service

```bash
make start # service starts via the shell on port 8001 and auto-reloads
```

### Starting service via docker-compose

```bash
docker-compose down postgres  # if you have started postgres with `make db` there will be issues
docker-compose build student-svc # if it hasn't been built
docker-compose up -d student-svc # starts on port 8002, -d is optional to run in demon mode
                                 # service auto-reloads
```

### Run tests

```bash
make test
```

### Fix formatting

```bash
make fix
```

### Lint

```bash
make lint
```

### Clean

```bash
make clean
```
