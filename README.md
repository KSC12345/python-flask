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

AWS Deployment:
https://www.youtube.com/watch?v=a1nnZDps_yM&ab_channel=ProgrammingwithAlex
https://github.com/cloudacademy/python-flask-microservices/tree/master/user-service

https://nishankkoul.hashnode.dev/end-to-end-cicd-pipeline-on-aws-for-a-flask-application
