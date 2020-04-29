up:
	docker-compose up --build

test:
	docker exec -it wine-app pytest

down:
	docker-compose down -v

loaddata:
	docker exec -it wine-app python ./dataset/load.py