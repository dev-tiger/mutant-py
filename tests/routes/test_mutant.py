import os
import datetime
import json
from unittest import TestCase

from app import create_app
from api.models import db


class TestMutant(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()

    def test_mutant(self):
        post = self.app.post(
            '/api/mutant',
            data=json.dumps({"dna": ["ATGCGA", "CAGTGC", "TTGTGT", "AGAAAG", "CCTCTA", "TCACTG"]}),
            headers={'Content-Type': 'application/json'}
        )

        response = {"message": "DNA already exist"}

        self.assertEqual(response, post.get_json())
