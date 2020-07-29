train:
	python app.py

server:
	export FLASK_APP=app
	export FLASK_ENV=development
	flask run --port 8080

ngrok:
	ngrok http 8080