#Start Using requirements.txt
export 
venv:
	python3 -m venv venv
	chmod +x venv/bin/activate
	. ./venv/bin/activate
install:
	#install commands
	pip3 install --upgrade pip &&\
	pip3 install -r requirements.txt
deploy: 
	python3 start.py
deploy_local: 
	ENV=development python3 start.py
local: venv install deploy_local
prod: venv install deploy

#End Using requirements.txt


#Start Using PIPENV
pipenvinstall:
	pipenv install --deploy --ignore-pipfile

deploy_prod_pip: 
	pipenv run python3 start.py
deploy_local_pip: 
	ENV=development pipenv run python3 start.py

local_pip: pipenvinstall deploy_local_pip
prod_pip: pipenvinstall deploy_prod_pip

#End Using PIPENV

format:

lint:

test:





