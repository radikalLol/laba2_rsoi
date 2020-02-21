import unittest
import os
import json
from ..app import create_app, db


class UsersTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app("testing")
        self.client = self.app.test_client
        self.user = {
            'name': 'Donya',
            'email': 'email777@mail.com',
            'password': 'passw0rd!'
        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.assertTrue(json_data.get('jwt_token'))
        self.assertEqual(res.status_code, 201)

    def test_user_creation_with_existing_email(self):
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('error'))

    def test_user_creation_with_no_password(self):
        user1 = {
            'name': 'Donya',
            'email': 'email777@mail.com',
        }
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('password'))
        
    def test_user_login(self):
                res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
                self.assertEqual(res.status_code, 201)
                res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
                json_data = json.loads(res.data)
                self.assertTrue(json_data.get('jwt_token'))
                self.assertEqual(res.status_code, 200)

    def test_user_login_with_invalid_password(self):
        """ User Login Tests with invalid credentials """
        user1 = {
            'password': 'eeeeeeee',
            'email': 'email777@mail.com',
        }
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertFalse(json_data.get('jwt_token'))
        self.assertEqual(json_data.get('error'), 'invalid credentials')
        self.assertEqual(res.status_code, 400)

    def test_user_login_with_invalid_email(self):
        """ User Login Tests with invalid credentials """
        user1 = {
            'password': 'passw0rd!',
            'email': 'osirfkasssl.com',
        }
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertFalse(json_data.get('jwt_token'))
        self.assertEqual(json_data.get('error'), 'invalid credentials')
        self.assertEqual(res.status_code, 400)

    def test_user_get_me(self):
        """ Test User Get Me """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')
        res = self.client().get('/api/v1/users/me',
                                headers={'Content-Type': 'application/json', 'api-token': api_token})
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('email'), 'email777@mail.com')
        self.assertEqual(json_data.get('name'), 'Donya')

    def test_user_update_me(self):
        """ Test User Update Me """
        user1 = {
            'name': 'new name'
        }
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')
        res = self.client().put('/api/v1/users/me',
                                headers={'Content-Type': 'application/json', 'api-token': api_token},
                                data=json.dumps(user1))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_data.get('name'), 'new name')

    def test_delete_user(self):
        """ Test User Delete """
        res = self.client().post('/api/v1/users/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        api_token = json.loads(res.data).get('jwt_token')
        res = self.client().delete('/api/v1/users/me',
                                   headers={'Content-Type': 'application/json', 'api-token': api_token})
        self.assertEqual(res.status_code, 204)

    def tearDown(self):
        """
            Tear Down
            """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    if __name__ == "__main__":
        unittest.main()
