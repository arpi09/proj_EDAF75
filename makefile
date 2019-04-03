server:
	python app.py
	
reset:
	curl -X POST http://127.0.0.1:5000/reset

customers:
	curl -X GET http://127.0.0.1:5000/customers
	
ingredients:
	curl -X GET http://127.0.0.1:5000/ingredients

cookies:
	curl -X GET http://127.0.0.1:5000/cookies

recipes:
	curl -X GET http://127.0.0.1:5000/recipes

Berliner:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Berliner

pallets:
	curl -X GET http://127.0.0.1:5000/pallets












