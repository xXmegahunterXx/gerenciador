import unittest
from gerenciador import create_app, db
from gerenciador.models import User

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
            TESTING=True
        )
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='testuser')
            user.set_password('testpass')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_logout(self):
        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpass'
        ), follow_redirects=True)
        self.assertIn(b'Clientes', response.data)

        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Login', response.data)

if __name__ == '__main__':
    unittest.main()
