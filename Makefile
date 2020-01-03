psql:
	docker-compose exec db /bin/bash -c "psql -U test_user -d test_db"

newmigration:
	docker-compose exec -T backend /bin/bash -c "alembic -c alembic/alembic.ini revision --autogenerate -m '$(name)'"

migrate:
	docker-compose exec -T backend /bin/bash -c "/app/prestart.sh"
