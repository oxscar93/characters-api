# Character API

# Installation

Make sure you have the latest python 3 version installed. This project runs with python >= 3.12.4
Run `run python -m pipenv install`


# Startup
Run `python -m pipenv run python -m flask run`.
As default, the API will start on port 5000 and you can see the swagger documentation on `http://localhost:5000/apidocs`
A SQLLite database will be created by default if not exists in the base directory.


# Docker installation

Go to the base directory and run `docker build -t character_api .` 


# Docker startup

After building the image, go to the base directory and Run `docker run -p 5000:5000 character_api`