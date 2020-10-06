#FSND Capstone Project 

## Table of Contents

1. Motivation
2. Set up project locally
3. API Endpoints

## Motivation

This project encapsulates all the information that has been taught in the Udacity Full Stack Nanodegree. The project includes a database schema, automated tests, API endpoints, Authentication / Authorisation using Auth0 and deployment to Heroku. 

## How to Run the Project Locally 
To run the project locally, clone the project locally to your machine. 

You then need to change directory (cd) into the "starter" folder which contains all the files.

# Installing Dependencies

# Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

# Virtual Environment
Is it is recommended working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

# Pip Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

```
pip install -r requirements.txt
```

This will isntall of the required packages for this project that are within the requirement.txt file.

# Updating the Database URL
You will not be able to access Heroku when running the project locally therefore you must make some changes to the code base to connect to a local database. 

In app.py, models.py and test_app.py you will need to modify the "database_path". You can do this by replacing 

```
database_path = os.environ['DATABASE_URL']
```

with 

```
database_filename = "database.db"
  project_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
```

# Running the server
Within the "starter" directory, execute:

```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

You will now be able to hit the API endpoints locally. 

# Running the tests

Within the "starter" directory, execute: 

```
python test_app.py
```

## API Endpoints

The base url for the endpoints is:

```
https://movieprojectnat.herokuapp.com
```

```
GET '/actors' - requires permissions "read:actors"
GET '/movies' - requires permissions "read:movies"

POST '/actors' - requires permissions "write:actors"
POST '/movies' - requires permissions "write:movies"

Patch '/actors/<int:actor_id>/edit' - requires permissions "edit:actors"
Patch '/movies/<int:movie_id>/edit' - requires permissions "edit:movies"

DELETE '/movies/<int:movie_id>' - requires permissions "delete:actors"
DELETE '/actors/<int:actor_id>' - requires permissions "delete:movies"

```

GET '/actors'

- General:
    - Fetches a dictionary of actors
    - Request Arguments: None
    - Returns: An object with five keys:
        - id
        - name
        - surname
        - gender
        - age
- curl https://movieprojectnat.herokuapp.com/actors
- Example response: 
```
 
```
'GET '/movies'
- General:
    - Fetches a dictionary of movies. 
    - Request Arguments: None
    - Returns: An object with three keys:
        - id
        - title
        - release_date
- curl https://movieprojectnat.herokuapp.com/movies
-Example response:

```
  
```

POST '/actors'
- General:
    - Takes the following response body and adds a new actor to the list of actors:
    - Request Body:
    ```
        {
            name : string,
            surname : string,
            gender: string,
            age: int
        }
    ```
    - Example Response: 
    ```

    ```
POST '/actors'
- General:
    - Takes the following response body and adds a new movie to the list of movies:
    - Request Body:
    ```
        {
            title : string,
            release_date : string,
        }
    ```
    - Example Response: 
    ```

    ```

DELETE '/actors/<int:actor_id>'

- General:
    - Takes a actor id and deletes the actor associated with the actor id
    - curl -X DELETE https://movieprojectnat.herokuapp.com/actors/20
    - Request Body:
        ```
        {
            actor_id: actor_id
        }
        ```
    - Example Response: 

        ```
        {
            'success' : true,
            'deleted' : 20
        }

        ```

DELETE '/movies/<int:movie_id>'

- General:
    - Takes a movie id and deletes the movie associated with the movie id
    - curl -X DELETE https://movieprojectnat.herokuapp.com/movies/20
    - Request Body:
        ```
        {
            movie_id: movie_id
        }
        ```
    - Example Response: 

        ```
        {
            'success' : true,
            'deleted' : 20
        }

        ```

PATCH '/actors/<int:actor_id>/edit'
- General:
    - Takes the following response body and edits a movie in the list of movies:
    - Request Body:
    ```
        {
            title : string,
            release_date : string,
        }
    ```
    - Example Response: 
    ```

    ```


PATCH '/movies/<int:movie_id>/edit'
- General:
    - Takes the following response body and edits a movie in the list of movies:
    - Request Body:
    ```
        {
            title : string,
            release_date : string,
        }
    ```
    - Example Response: 
    ```

    ```


# Error Handling

The APIs handle the following errors: 

- 400: Bad Request
- 401: Unauthorised
- 404: Resource Not Found
- 422: Not Processable 

The error responses are in the following format: 

```
{
    "success": False,
    "error": <error code>,
    "message": <error message>
}
```

## Authentication 

Auth0 is used to handle the Authentication and Authorisation for the API endpoints. You may need to set up Auth0 to access the API endpoints when running the app locally and create the roles below along with the permissions required for each API call. 

There are three distinct roles for this project:

1. Casting Assistant
    - Can view actors and movies
2. Casting Director 
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
3. Executive Director
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

