# fastapi_sqlalchemy_alembic
POC for database migration using alembic tool in fastapi

create .env file and add

    DATABASE_URL = postgresql+psycopg2://{username}:{password}@db:5432

step-1:

    docker-compose build

step-2:

    docker-compose run web alembic revision --autogenerate -m "first migration added"


step-3:

    docker-compose run web alembic upgrade head


step-4:

    docker-compose up

check in pgadmin with login with creds in docker file
