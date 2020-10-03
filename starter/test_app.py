import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app


from models import setup_db, Movie, Actor

class CapstoneProjectTests(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}/{}".format('postgres:@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    '''Happy Path Tests'''   

    # Get Tests

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #self.assertTrue(data['movies'])


    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #self.assertTrue(data['actor'])

    # Delete Tests

    def test_delete_actor(self):

        TestActor = Actor(name='test', surname = 'test', gender="male", age=1)

        TestActor.insert()
        actor = Actor.query.get(TestActor.id)
        actor_id = actor.id

        res = self.client().delete(f'/actors/{actor_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], actor_id)

    def test_delete_movie(self):

        TestMovie = Movie(title='test', release_date = '01-01-01')
        TestMovie.insert()
        movie = Movie.query.get(TestMovie.id)
        movie_id = movie.id

        res = self.client().delete(f'/movies/{movie_id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], movie_id)

    # Post Tests
    def test_create_actor(self):
        res = self.client().post('/actors', json = {'name' : 'testing', 'surname':'testing', 'gender' : 'male', 'age':1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        res = self.client().post('/movies', json = {'title' : 'testing', 'release_date':'01-01-01'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Patch Tests

    def test_patch_movie(self):
        res = self.client().patch('/movies/1/edit', json = {'title' : 'testier'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor(self):
        res = self.client().patch('/actors/1/edit', json = {'name' : 'testier'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    '''Unhappy Path Tests'''   

    # Delete non existent entry

    def test_404_delete_actor(self):
        res = self.client().delete(f'/actors/5')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_404_delete_movie(self):
        res = self.client().delete(f'/movies/5')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent movie
    def test_404_update_movie(self):
        res = self.client().patch(f'/movies/5/edit', json = {'title' : 'testier'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent actor

    def test_404_update_actor(self):
        res = self.client().patch(f'/actors/5/edit', json = {'surname' : 'testier'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update movie without payload

    def test_422_update_movie(self):
        res = self.client().patch(f'/movies/1/edit')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # update actor without payload

    def test_422_update_actor(self):
        res = self.client().patch(f'/actors/1/edit')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # create actor without payload

    def test_422_create_actor(self):
        res = self.client().post(f'/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')    

    # create actor without payload

    def test_422_create_movie(self):
        res = self.client().post(f'/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')    