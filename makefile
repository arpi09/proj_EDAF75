main: 
	curl -X GET http://localhost:5000/ping
	# 
	#
	# 
	# 
	curl -X POST http://localhost:5000/reset
	# 
	#
	# 
	# 
	curl -X GET http://localhost:5000/movies
	# 
	#
	# 
	# 
	curl -X GET http://localhost:5000/movies?title=Spotlight"&"year=2015
	# 
	#
	# 
	# 
	curl -X GET http://localhost:5000/movies/tt5580390
	# 
	#
	# 
	# 
	curl -X POST http://localhost:5000/performances?imdb=tt5580390"&"theater=Kino"&"date=2019-02-22"&"time=19:00
	# 
	#
	# 
	# 
	curl -X GET http://localhost:5000/performances	
	# 
	#
	# 
	# 
	 




a:
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=0affb7c0266ddd05dc937071e13d0598"&"pwd=dobido
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=18711855e59d3562de7953b4cc3a5886"&"pwd=dobido
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=44e018b24f2b29e76eb0c7e009bffad6"&"pwd=dobido
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=5fc53959ecaebb61cf89caedf40dd6f6"&"pwd=dobido
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=c31f407ceb3ab3ca62d8f5f3202a8d06"&"pwd=dobido
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=c4bce4f302c965a3755d919d1a6a151b"&"pwd=dobido
b:
	curl -X GET http://localhost:5000/customers/alice/tickets
c:
	curl -X POST http://localhost:5000/tickets?user=alice"&"performance=c4bce4f302c965a3755d919d1a6a151b"&"pwd=dobido
	

d:
		curl -X GET http://localhost:5000/performances	





















