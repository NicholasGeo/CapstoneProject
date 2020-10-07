#FSND Capstone Project 

## Table of Contents

1. Motivation
2. Set up project locally
3. Authentication
4. API Endpoints

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

## API Endpoints

The base url for the endpoints is:

```
https://projectactors.herokuapp.com
```

To hit the API endpoint you will need to use the following JWT tokens. Please note that these were created on the 07/10/2020 and will expire in 7 days.
```
casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4MGE1ZGY0YmEwMDY5MjJlNmZkIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU0NTcsImV4cCI6MTYwMjE1MTg1NywiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.upLQ1BlKP3BzfQh1DklXFyLof3RiMSqND5Hsz1iYlpMsfzfhPaS-vGBhl-iYLr9n2V7DNCfpt076IVZJ7WdyyMytS-pEapDy0DCMqsstLNiysbidfUZLVnLWEhmWqKOV8Ozt12VhNGsACUHXnVasIIeOLyIwKbG3avEc-BatjoYWegyPVE4l8WJDbn5Saqam-wlA1Z0EGV6uyLn2ETS2OCVDErTn-yG18ZU9HRn0Lnz7nqWSlwKyCvPWKPRUnYhiNfY5q4RxBsedfEcwTN0P7QvFGqQS623Qsp1WM9XJf6HlAwexnm193JWh89mfDD-qJ-w9JEjHw-IeStAsgqtC0Q'

casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4M2ZhNmFmNjQwMDcxZDkzZGFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU1MjUsImV4cCI6MTYwMjE1MTkyNSwiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.XncxdYV8SNLtq-Te3OCKcegq96UEK5Qao2I8QmLUkaHQOSS_VJlT7MelKUkxeM-CmQXWnnn05071nyN77sbEvMz7AaWyUz2gxToxYpiIUi6cuFXYnRm2uRDenHw-h7_969hgmHxClC50yHD18JEuyfiQfHk1UShZiHjvZ-BhhPt03M7sbGM8DmSIzMd648_Rgctkkc0TAjU9nSNMCssFJjX62kQIahzTTbklWqdI2sSFr-lSXrXkgd7keDOQgpXirCffi8mpr39HfNf4F0e4iCTXnB5SbygeQlgsEOsanG-ZPnR4RX62nDv33NzOrA7i74UQTIC_lgI-nQwvE33HJA'

casting_executive_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4NTU1MmNiNTUwMDc4NDg1MzNiIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU1OTksImV4cCI6MTYwMjE1MTk5OSwiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.iKRB7gwtPkGV92sb_69zspT8fzxc3h-pFRiW5liSoMhPQxSPdJhO6EYIKrjyV-lPkf55NtGTLyIJtGI7HppjWv3ApkzDZ7sqMYDY_kQBL9F5HO17OD2R2EBmKYHwvxIxblxRcZjuVKRMgdysyae5e8LwqRf0da62XkR7VUnw5qd943lK2ohqAaTdwycTBloTC5bFbCVUsykBcs6O81x2dSY0iFz_13xS6W4KGB2HvZSWucYZGTRnPtHt1daOZSm-iIdn5-B6CKfjPKXE0BOp1vZrW2Hio1SscPjuylpySHqX7GI2I7hyrup6318bq7TYyzhI2a9WGSueworDYFXtIA'
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
- curl https://projectactors.herokuapp.com/actors
- Example response: 
```
{
    "actor": {
        "id": 1,
        "name": "test",
        "surname": "test"
        "age": 1
        "gender": "test"
    },
    "success": true
}
 
```
'GET '/movies'
- General:
    - Fetches a dictionary of movies. 
    - Request Arguments: None
    - Returns: An object with three keys:
        - id
        - title
        - release_date
- curl https://projectactors.herokuapp.com/movies
-Example response:

```
{
    "movie": {
        "id": 1,
        "title": "test",
        "release_date": "01-01-01"

    },
    "success": true
}
  
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
        {
          'success': True,
          'actor': new_actor.name
        }
    ```
POST '/MOVIES '
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
    {
        "success": True,
        "title": "test",
        "release_date": "01-01-01"

    }

    ```

DELETE '/actors/<int:actor_id>'

- General:
    - Takes a actor id and deletes the actor associated with the actor id
    - curl -X DELETE https://projectactors.herokuapp.com/actors/20
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
    - curl -X DELETE https://projectactors.herokuapp.com/movies/20
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
    {
        "success": True,
        "movie": {
            "id": 1,
            "title": "test",
            "release_date": "01-01-01"
        }
    }

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
    {
        "success": True,
        "actor": {
            "id": 1,
            "name": "test",
            "surname": "test"
            "age": 1
            "gender": "test"
            }
    }

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





