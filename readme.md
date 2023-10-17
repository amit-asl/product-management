## ASL Product Management
Product Management application with the help of celery to automate scheduling jobs.

To run the project:

> sudo docker compose up

*sudo is not needed for windows

**Hit on the `/docs` to test the crud operations**

[Note: Please check if the ports are occupied in the localhost before attempting the above command]

#### Tech Stack:
* python
* celery
* postgres
* redis

#### Dockerfile Description
In the dockerfile there are five services. Two are from celery called celery_beat and celery_worker. Other three are as follows, python web app, postgres and redis. Redis is being the message broker here. Postgres as a the persistent storage is being used in the project. 
The application runs without any dependency. Celery services depends on other services. Postgres and Redis runs independently as well.

#### Testing
There is a tests folder which is for the unit tests.
This tests can be invoked using the `pytest` command in the root folder.

#### Implemented Auxiliary Functionalites:
* Logs (through `logging` module)
* Tests (through `pytest` module)
* Gitops* (through `github actions`)

[Note: As of now the logs are created per-minute for demonstration]
#### TODO:
- Build the project structure. [DONE]
- Make a demo endpoint work. [DONE]
- Setup the backend with postgresql to store the data. [DONE]
- Make endpoint for CRUD operation. [DONE]
- Make a Scheduler with Celery. [DONE]
- Dockerize the entire project. [DONE]