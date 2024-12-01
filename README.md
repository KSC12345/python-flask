1. Create a Python Virtual Environment
    `python -m venv ~/.venv or virtualenv ~/.venv`
2.Create emmty files:`requirements.txt,Makefile`
3.Freeze pip module versions: `pip freeze > requirements.txt`
4.install application :`make install`
5. Run application in local: `make local`

##### Using PIPENV #######

1.Install pipenv : `pip install pipenv`
2.Create and activate virtual environment: `pipenv shell`
3.Install dev packaages :`pipenv install pytest --dev`
4.Install packaages :`pipenv install pytest`
5.once installed all packages run the lock: `pipenv lock`

###### Run Application ######

1. Run Application : `make local_pip`

Tutorial : `https://realpython.com/pipenv-guide/`
https://www.youtube.com/watch?v=zDYL22QNiWk&ab_channel=CoreySchafer

MongoDB Setup URL : https://www.youtube.com/watch?v=8gUQL2zlpvI&ab_channel=ProgrammingKnowledge

MongoDB Path:mongod --dbpath=<PATH>/data/db

