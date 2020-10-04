import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app


from models import setup_db, Movie, Actor

casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4MGE1ZGY0YmEwMDY5MjJlNmZkIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDE4MTg4ODcsImV4cCI6MTYwMTgyNjA4NywiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.FEd3OP7eVu6HXG3KR0s3P6P-RJm_y573ZdtGaEKslwWGBXVeI3xg73h9V1lXrU7iwG7DxBxVbZGUow0WRbEHAIeth0n_n4YaPVIhQQ-2C6IeWD04vZnA4E89wrg-GVE1UB1Q8VFpDH7X0kzT6J-e8FrlwleWYay4PAQPS-8h9rxydPvLdn3KTWq5YBYPYlw5eyJEPHpcCNEd1q9w9CYAVN5v1SJmAgV9XLaVkPbD-YICxcugsuhJkfYa4KA4C7b0NBj2WBvYBLvvhii9zCj7hnQE_LaNlwBbyAH48PQHZeOpFuHqa3dTvdcQpplU_Ucbi4y9_Wz8f_Emc4pSvWBbaw'
casting_director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4M2ZhNmFmNjQwMDcxZDkzZGFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDE4MTg5NTcsImV4cCI6MTYwMTgyNjE1NywiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.QG1X1ykMgPL6dtfIOdYKWHx1WteXqpuVK-CJy9eIb-RHVLd3WqE0AnreXgCHZjL0t7DyKZnqGW3i_HpaLtBhIdT064OBIaWj3F5oVMa52DfQf9I04qE9XGMjlb4gifn1lWr8nRZLBNlf19coWcVnGzKNe6C84VxvXbTdTrUrSnS3oo7GWxshSAsnBYR5xSjNJWuIvaAN37Cm1nXujeCr5iBbpoLUlFgsj5M3qqlI9vXhhV6s6feihuwFbaPdN9S7J8hK6Nh6PsHkfiv3QEASSLgoCV7dg47jHXIs14pY2hqQoaNqFA_C2WNMJhqIE8KztghPNCO93qYtKEAdTYUeIA'
casting_executive_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4NTU1MmNiNTUwMDc4NDg1MzNiIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDE4MTkwNDcsImV4cCI6MTYwMTgyNjI0NywiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.JN_tWPtAX6iZmKcx4pZo1WdVsxjKyiIHhoLKuFMNMjASYnuFFsWypucsAWon1Sjd_gXHZLDkZo3LAjHQ4uWgJPs--CipX2Syg5FnVwf5M2Bl6fom6hR6fZ9jSFCnym8VJQV1800r7NFTjZYegHtNJYWZ0KqvbywFadHoUpMlECS5HQwfFz-Sq8fLA13tmOYltvPHYWtmKoW442C8czSfXW1zh2is5eZkyFBOecVyHtENFpO9V-Pu7o9lf1KaLxRpwqomODls7JBq3Uvs6ruR5UBBEdqkNYI95hivFcDE_MoIj1-CSPW-q8kgq9zTPi5HFlppfsJLZ3zJRfZTUqqkOQ'

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
        res = self.client().get('/movies', headers = { 'Authorization': casting_assistant_token })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])


    def test_get_actors(self):
        res = self.client().get('/actors', headers = { 'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Delete Tests

    def test_delete_actor(self):

        TestActor = Actor(name='test', surname = 'test', gender="male", age=1)

        TestActor.insert()
        actor = Actor.query.get(TestActor.id)
        actor_id = actor.id

        res = self.client().delete(f'/actors/{actor_id}', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], actor_id)

    def test_delete_movie(self):

        TestMovie = Movie(title='test', release_date = '01-01-01')
        TestMovie.insert()
        movie = Movie.query.get(TestMovie.id)
        movie_id = movie.id

        res = self.client().delete(f'/movies/{movie_id}', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], movie_id)

    # Post Tests
    def test_create_actor(self):
        res = self.client().post('/actors', json = {'name' : 'testing', 'surname':'testing', 'gender' : 'male', 'age':1}, headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        res = self.client().post('/movies', json = {'title' : 'testing', 'release_date':'01-01-01'}, headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Patch Tests

    def test_patch_movie(self):
        res = self.client().patch('/movies/1/edit', json = {'title' : 'testier'}, headers = { 'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor(self):
        res = self.client().patch('/actors/1/edit', json = {'name' : 'testier'}, headers = { 'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    '''Unhappy Path Tests'''   

    # Delete non existent entry

    def test_404_delete_actor(self):
        res = self.client().delete(f'/actors/5', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_404_delete_movie(self):
        res = self.client().delete(f'/movies/5', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent movie
    def test_404_update_movie(self):
        res = self.client().patch(f'/movies/5/edit', json = {'title' : 'testier'} , headers = { 'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent actor

    def test_404_update_actor(self):
        res = self.client().patch(f'/actors/5/edit', json = {'surname' : 'testier'}, headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update movie without payload

    def test_422_update_movie(self):
        res = self.client().patch(f'/movies/1/edit', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # update actor without payload

    def test_422_update_actor(self):
        res = self.client().patch(f'/actors/1/edit', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # create actor without payload

    def test_422_create_actor(self):
        res = self.client().post(f'/actors', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')    

    # create actor without payload

    def test_422_create_movie(self):
        res = self.client().post(f'/movies', headers = { 'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')    

    '''Auth / Authz Tests'''

    # create actor with the wrong permissions

    def test_create_actor_401(self):
        res = self.client().post('/actors', json = {'name' : 'testing', 'surname':'testing', 'gender' : 'male', 'age':1}, headers = { 'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found in payload')

    # delete movie with the mising permissions

    def test_delete_actor_401(self):
        res = self.client().delete(f'/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ' Authorisation header is expected')

    # update actor with the wrong permission 
    def test_patch_actors_401(self):
        res = self.client().patch('/actors/1/edit', json = {'name' : 'testier'}, headers = { 'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found in payload')

    # update movie with the wrong permission 
    def test_patch_movie_401(self):
        res = self.client().patch('/movies/1/edit', json = {'title' : 'testier'}, headers = { 'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found in payload')

    # get all movies without permissions
    def test_get_movies_401(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ' Authorisation header is expected')

    # get all actors without permissions
    def test_get_actors_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], ' Authorisation header is expected')