# Character API

# Installation

Make sure you have the latest python 3 version installed. This project runs with python >= 3.12.4  
Run `python -m pipenv install`



# Startup
Run `python -m pipenv run python -m flask run`  
As default, the API will start on port 5000 and a SQLite database will be created by default if not exists in the base directory.


# Docker installation

Go to the base directory (/character-api) and run `docker build -t character_api .` 


# Docker startup

After building the image, go to the base directory (/character-api) and run `docker run -p 5000:5000 character_api`


# Api documentation

In docs folder you can find a postman collection you can use for the API. Also, you can navigate the swagger documentation located on `http://localhost:5000/apidocs`.
