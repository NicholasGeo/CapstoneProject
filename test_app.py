import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app


from models import setup_db, Movie, Actor

casting_assistant_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4MGE1ZGY0YmEwMDY5MjJlNmZkIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU0NTcsImV4cCI6MTYwMjE1MTg1NywiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiXX0.upLQ1BlKP3BzfQh1DklXFyLof3RiMSqND5Hsz1iYlpMsfzfhPaS-vGBhl-iYLr9n2V7DNCfpt076IVZJ7WdyyMytS-pEapDy0DCMqsstLNiysbidfUZLVnLWEhmWqKOV8Ozt12VhNGsACUHXnVasIIeOLyIwKbG3avEc-BatjoYWegyPVE4l8WJDbn5Saqam-wlA1Z0EGV6uyLn2ETS2OCVDErTn-yG18ZU9HRn0Lnz7nqWSlwKyCvPWKPRUnYhiNfY5q4RxBsedfEcwTN0P7QvFGqQS623Qsp1WM9XJf6HlAwexnm193JWh89mfDD-qJ-w9JEjHw-IeStAsgqtC0Q'
casting_director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4M2ZhNmFmNjQwMDcxZDkzZGFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU1MjUsImV4cCI6MTYwMjE1MTkyNSwiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.XncxdYV8SNLtq-Te3OCKcegq96UEK5Qao2I8QmLUkaHQOSS_VJlT7MelKUkxeM-CmQXWnnn05071nyN77sbEvMz7AaWyUz2gxToxYpiIUi6cuFXYnRm2uRDenHw-h7_969hgmHxClC50yHD18JEuyfiQfHk1UShZiHjvZ-BhhPt03M7sbGM8DmSIzMd648_Rgctkkc0TAjU9nSNMCssFJjX62kQIahzTTbklWqdI2sSFr-lSXrXkgd7keDOQgpXirCffi8mpr39HfNf4F0e4iCTXnB5SbygeQlgsEOsanG-ZPnR4RX62nDv33NzOrA7i74UQTIC_lgI-nQwvE33HJA'
casting_executive_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVEaDJNMVFMcmV3WDdhMThsZFZzSyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNWs1YWs4NC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3OGY4NTU1MmNiNTUwMDc4NDg1MzNiIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MDIwNjU1OTksImV4cCI6MTYwMjE1MTk5OSwiYXpwIjoibVNHZEU0QUVGd3Rxd3VDeEoxTE10UGVaT1Z3ZzlyZEMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.iKRB7gwtPkGV92sb_69zspT8fzxc3h-pFRiW5liSoMhPQxSPdJhO6EYIKrjyV-lPkf55NtGTLyIJtGI7HppjWv3ApkzDZ7sqMYDY_kQBL9F5HO17OD2R2EBmKYHwvxIxblxRcZjuVKRMgdysyae5e8LwqRf0da62XkR7VUnw5qd943lK2ohqAaTdwycTBloTC5bFbCVUsykBcs6O81x2dSY0iFz_13xS6W4KGB2HvZSWucYZGTRnPtHt1daOZSm-iIdn5-B6CKfjPKXE0BOp1vZrW2Hio1SscPjuylpySHqX7GI2I7hyrup6318bq7TYyzhI2a9WGSueworDYFXtIA'


class CapstoneProjectTests(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = os.environ['DATABASE_URL']
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
        res = self.client().get(
            '/movies',
            headers={
                'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_actors(self):
        res = self.client().get(
            '/actors',
            headers={
                'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Delete Tests

    def test_delete_actor(self):

        TestActor = Actor(name='test', surname='test', gender="male", age=1)

        TestActor.insert()
        actor = Actor.query.get(TestActor.id)
        actor_id = actor.id

        res = self.client().delete(
            f'/actors/{actor_id}',
            headers={
                'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], actor_id)

    def test_delete_movie(self):

        TestMovie = Movie(title='test', release_date='01-01-01')
        TestMovie.insert()
        movie = Movie.query.get(TestMovie.id)
        movie_id = movie.id

        res = self.client().delete(
            f'/movies/{movie_id}',
            headers={
                'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], movie_id)

    # Post Tests
    def test_create_actor(self):
        res = self.client().post(
            '/actors',
            json={
                'name': 'testing',
                'surname': 'testing',
                'gender': 'male',
                'age': 1},
            headers={
                'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie(self):
        res = self.client().post(
            '/movies',
            json={
                'title': 'testing',
                'release_date': '01-01-01'},
            headers={
                'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Patch Tests

    def test_patch_movie(self):
        res = self.client().patch(
            '/movies/1/edit',
            json={
                'title': 'testier'},
            headers={
                'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor(self):
        res = self.client().patch(
            '/actors/1/edit',
            json={
                'name': 'testier'},
            headers={
                'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    '''Unhappy Path Tests'''

    # Delete non existent entry

    def test_404_delete_actor(self):
        res = self.client().delete(f'/actors/5',
                                   headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_404_delete_movie(self):
        res = self.client().delete(f'/movies/5',
                                   headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent movie
    def test_404_update_movie(self):
        res = self.client().patch(
            f'/movies/5/edit',
            json={
                'title': 'testier'},
            headers={
                'Authorization': casting_director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update non-existent actor

    def test_404_update_actor(self):
        res = self.client().patch(
            f'/actors/5/edit',
            json={
                'surname': 'testier'},
            headers={
                'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    # update movie without payload

    def test_422_update_movie(self):
        res = self.client().patch(f'/movies/1/edit',
                                  headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # update actor without payload

    def test_422_update_actor(self):
        res = self.client().patch(f'/actors/1/edit',
                                  headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # create actor without payload

    def test_422_create_actor(self):
        res = self.client().post(f'/actors',
                                 headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # create actor without payload

    def test_422_create_movie(self):
        res = self.client().post(f'/movies',
                                 headers={'Authorization': casting_executive_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''Auth / Authz Tests'''

    # create actor with the wrong permissions

    def test_create_actor_401(self):
        res = self.client().post(
            '/actors',
            json={
                'name': 'testing',
                'surname': 'testing',
                'gender': 'male',
                'age': 1},
            headers={
                'Authorization': casting_assistant_token})
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
        res = self.client().patch(
            '/actors/1/edit',
            json={
                'name': 'testier'},
            headers={
                'Authorization': casting_assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found in payload')

    # update movie with the wrong permission
    def test_patch_movie_401(self):
        res = self.client().patch(
            '/movies/1/edit',
            json={
                'title': 'testier'},
            headers={
                'Authorization': casting_assistant_token})
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
