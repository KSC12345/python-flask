install:
	#install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

format:

lint:

test:

deploy: 
	python3 start.py
	
local: install deploy

all:install lint test deploy