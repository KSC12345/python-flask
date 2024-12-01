venv:
	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
install:
	#install commands
	pip3 install --upgrade pip &&\
	pip3 install -r requirements.txt
format:

lint:

test:

deploy: 
	python3 start.py
deploy_local: 
	ENV=development python3 start.py	
local: venv install deploy_local
prod:  venv install deploy