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
GET '/actors'
GET '/movies'

POST '/actors'
POST '/movies'

Patch '/actors/<int:actor_id>/edit'
Patch '/movies/<int:movie_id>/edit'

DELETE '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'

```

GET '/actors'

- General:
    - Fetches a dictionary of actors in which the keys are the ids  and the value is the corresponding string of the actors
    - Request Arguments: None
    - Returns: An object with a single key, actors, that contains a object of id: category_string key:value pairs.
- curl http://127.0.0.1:5000/categories
- Example response: 
```
 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
'GET '/questions'
- General:
    - Fetches a dictionary of paginated questions, displaying 10 results per page. 
    - Fetches a list of the categories which the key is the id of the cateogry and the value is the type of the category. 
    - Fetches the total number of questions
    - Request Arguments: None
    - Returns: An object with a four keys, categories, current_cateogories, questions, total_questions.
- curl http://127.0.0.1:5000/questions
-Example response:

```
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_categories": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 45
}

```
GET '/categories/<category_id>/questions'
- General:
    - Fetches the current category
    - Fetches a dictionary of questions linked the category passed in "category_id".  
    - Fetches the total number of questions
    - Request Arguments: None
    - Returns: An object with a four keys, categories, current_cateogories, questions, total_questions.
- curl http://127.0.0.1:5000/categories/1/questions
- Example response:
```  
  "current_category": 2,
  "questions": [
    {
      "answer": "test",
      "category": 1,
      "difficulty": 1,
      "id": 25,
      "question": "test"
    },
    {
      "answer": "test",
      "category": 1,
      "difficulty": 1,
      "id": 26,
      "question": "test"
    },
  ],
  "success": true,
  "total_questions": 2
}

```

POST '/questions'
- General:
    - Takes the following response body and adds a new question to the list of questions:
    - Request Body:
    ```
        {
            questions : string,
            answer : string,
            difficulty: int,
            category: string
        }
    ```
    - Example Response: 
    ```
        {
            question : question,
            new_question_id: question_id,
            success: true
        }
    ```
POST '/questions/search'
- General:
    - Takes a search term and fetches all the questions which have a matching substring to the search term
    - curl -d {"searchTerm":"what"}  -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/questions/search
    - Request Body:
    ```
        {
            searchTerm : string
        }
    ```
    - Example Response:

    ```
    "current_category": null,
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },

    ],
    "success": true,
    "total_questions": 2
    }
 
    ```

DELETE '/questions/<int:question_id>'

- General:
    - Takes a question id and deletes the question associated with the question id
    - curl -X DELETE http://127.0.0.1:5000/questions/20
    - Request Body:
        ```
        {
            questions_id: question_id
        }
        ```
    - Example Response: 

        ```
        {
            'success' : true,
            'deleted' : 20
        }

        ```

POST '/quizzes'
- General:
    - Takes a previous question and a category and returns a random question excluding any previous questions that have been returned
    - curl -d '{"previous_questions": [], "quiz_category":"Entertainment", "id": 5 }' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/quizzes
    - Request Body: 
    ```
    {
        "previous_question" : [<list of previously asked question ids>]
        "quiz_category" : id and type of the category the question will be from in the form of: {type:string, id:int }
    }
    ```
    - Example Response:
    ```
    "questions": {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
   "success": true
}

    ```



# Error Handling

The APIs handle the following errors: 

- 400: Bad Request
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


