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

recipes:
	curl -X GET http://127.0.0.1:5000/recipes

ingredients:
	curl -X GET http://127.0.0.1:5000/ingredients



	
Nut_ring:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Nut\ ring
Nut_cookie:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Nut\ cookie
Amneris:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Amneris
Tango:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Tango
Almond_delight:
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Almond\ delight




# // to do

customers:
	curl -X GET http://127.0.0.1:5000/customers
	


test:
	make reset
	curl -X POST http://127.0.0.1:5000/pallets\?cookie\=Berliner