server:
	python app.py

# // implemented
reset:
	curl -X POST http://127.0.0.1:5000/reset

cookies:
	curl -X GET http://127.0.0.1:5000/cookies

Berliner:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Berliner

pallets:
	curl -X GET http://127.0.0.1:5000/pallets

specific_pallet:
	curl -X GET http://localhost:5000/pallets\?cookie\=Berliner\&blocked\=0\&after\=2020-03-03

recipes:
	curl -X GET http://127.0.0.1:5000/recipes

ingredients:
	curl -X GET http://127.0.0.1:5000/ingredients











# // to do

customers:
	curl -X GET http://127.0.0.1:5000/customers
