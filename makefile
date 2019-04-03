server:
	python app.py

# // implemented
reset:
	curl -X POST http://127.0.0.1:8888/reset

cookies:
	curl -X GET http://127.0.0.1:8888/cookies

Berliner:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Berliner

pallets:
	curl -X GET http://127.0.0.1:8888/pallets

specific_pallet:
	curl -X GET http://localhost:8888/pallets\?cookie\=Berliner\&blocked\=0\&after\=2020-03-03

recipes:
	curl -X GET http://127.0.0.1:8888/recipes

ingredients:
	curl -X GET http://127.0.0.1:8888/ingredients




Nut_ring:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Nut+ring
Nut_cookie:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Nut+cookie
Amneris:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Amneris
Tango:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Tango
Almond_delight:
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Almond+delight




# // to do

customers:
	curl -X GET http://127.0.0.1:8888/customers



test:
	make reset
	curl -X POST http://127.0.0.1:8888/pallets\?cookie\=Berliner

create_db:
	sqlite3 data.db < code.sql
