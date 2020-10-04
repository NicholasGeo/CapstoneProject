import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import *
from auth import AuthError, requires_auth

def create_app(test_config=None):

  app = Flask(__name__)
  database_filename = "database.db"
  project_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db = SQLAlchemy(app)

  '''
  @TODO uncomment the following line to initialize the datbase
  !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
  !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
  '''
  #db_drop_and_create_all()

  # ROUTES
  '''
  TODO: implement the routes and the endpoints 
  '''

  # Get the movies

  @app.route('/movies', methods = ['GET'])
  @requires_auth('read:movies')
  def get_movies(token): 
    movies = Movie.query.all()
    movies = [movie.format() for movie in movies]

    return jsonify({
      'success': True,
      'movies': movies
    }), 200


  # Get the actors

  @app.route('/actors', methods = ['GET'])
  @requires_auth('read:actors')
  def get_actors(token): 
    actors = Actor.query.all()
    actors = [actor.format() for actor in actors]

    return jsonify({
      'success': True,
      'actors': actors
    }), 200

  # Delete an actor

  @app.route('/actors/<int:id>', methods = ['DELETE'])
  @requires_auth('delete:actor')
  def delete_actors(token, id): 
    actor = Actor.query.get(id)

    if actor is None:
      abort(404)

    actor.delete()

    return jsonify({
      'success': True,
      'deleted': actor.id
    })

  # Delete a movie

  @app.route('/movies/<int:id>', methods = ['DELETE'])
  @requires_auth('delete:movie')
  def delete_movies(token, id): 
    movie = Movie.query.get(id)

    if movie is None:
      abort(404)

    movie.delete()

    return jsonify({
      'success': True,
      'deleted': movie.id
    })

  # Add a new actor

  @app.route('/actors',methods=['POST'])
  @requires_auth('create:actor')
  def add_actor(token):
      json_payload = request.get_json()

      if not json_payload:
          abort(422)

      name = json_payload.get('name')
      surname = json_payload.get('surname')
      age = json_payload.get('age')
      gender = json_payload.get('gender')

      new_actor= Actor(name=name, surname=surname, age=age, gender=gender)

      new_actor.insert()

      return jsonify({
          'success': True,
          'actor': new_actor.name
      })

  # Add a new movie

  @app.route('/movies',methods=['POST'])
  @requires_auth('create:movie')
  def add_movie(token):
      json_payload = request.get_json()

      if not json_payload:
         abort(422)

      title = json_payload.get('title')
      release_date = json_payload.get('release_date')
      #movie_id = json_payload['movie_id']
      #use json.dumps() here to change the recipe object into a string

      new_movie= Movie(title=title, release_date=release_date)

      new_movie.insert()

      return jsonify({
          'success': True,
          'movie': new_movie.format()
      })

  # update a movie 
  @app.route('/movies/<int:id>/edit',methods=['PATCH'])
  @requires_auth('edit:movies')
  def edit_movie(token, id):
      updated_movie = Movie.query.filter(Movie.id == id).one_or_none()

      if not updated_movie:
        abort(404)

      json_payload = request.get_json()

      if not json_payload:
          abort(422)

      if 'title' in json_payload:
        new_title = json_payload.get('title')
        updated_movie.title = new_title


      if 'release_date' in json_payload:
        release_date = json_payload.get('release_date')
        updated_movie.release_date = release_date


      #movie_id = json_payload['movie_id']
      #use json.dumps() here to change the recipe object into a string

      updated_movie.update()

      return jsonify({
          'success': True,
          'movie': updated_movie.format()
      })

  # update an actor 
  @app.route('/actors/<int:id>/edit',methods=['PATCH'])
  @requires_auth('edit:actors')
  def edit_actor(token, id):
      updated_actor = Actor.query.filter(Actor.id == id).one_or_none()

      if not updated_actor:
        abort(404)

      json_payload = request.get_json()

      if not json_payload:
          abort(422)

      if 'name' in json_payload:
        new_name = json_payload.get('name')
        updated_actor.name = new_name


      if 'surname' in json_payload:
        surname = json_payload.get('surname')
        updated_actor.surname = surname

      if 'age' in json_payload:
        age = json_payload.get('age')
        updated_actor.age = age

      if 'gender' in json_payload:
        gender = json_payload.get('gender')
        updated_actor.gender = gender


      #movie_id = json_payload['movie_id']
      #use json.dumps() here to change the recipe object into a string

      updated_actor.update()

      return jsonify({
          'success': True,
          'movie': updated_actor.format()
      })


  # Error Handling
  '''
  Example error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  '''
  @TODO implement error handlers using the @app.errorhandler(error) decorator
      each error handler should return (with approprate messages):
              jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  '''

  '''
  @TODO implement error handler for 404
      error handler should conform to general task above 
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False, 
          "error": 404,
          "message": "not found"
          }), 404

  @app.errorhandler(401)
  def unauthorised(error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "unauthorised"
          }), 401

        
  '''
  @TODO implement error handler for AuthError
      error handler should conform to general task above 
  '''
  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
          }), error.status_code

  return app

app = create_app()






