# fastapi_sqlalchemy_alembic
POC for database migration using alembic tool in fastapi

create .env file and add

    DATABASE_URL = postgresql+psycopg2://{username}:{password}@db:5432

docker-compose build

docker-compose run web alembic revision --autogenerate -m "first migration added"

docker-compose run web alembic upgrade head

docker-compose up

check in pgadmin with login with creds in docker file
