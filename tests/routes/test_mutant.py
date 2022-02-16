import json

from tests import BaseTest


class TestMutant(BaseTest):

    dna_mutant = {"dna": ["ATGCGA", "CGGGGC", "TTGGGT", "AGAAGG", "CCTCTG", "ATTTTG"]}
    dna_mutant2 = {"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAAG", "CCTCTA", "ATTTTG"]}
    dna_human = {"dna": ["ATGCGA", "CAGTGC", "TTGTGT", "AGAAAG", "CCTCTA", "TCACTG"]}
    dna_human2 = {"dna": ["ATTCGA", "CAGTGC", "TTGTGT", "AGAAAG", "CCTCTA", "TCACTG"]}

    def test_is_mutant(self):
        new_mutant = self.post_mutant(self.dna_mutant)
        response_message = {"message": "A mutant has been added"}
        self.assertEqual(200, new_mutant.status_code)
        self.assertEqual(response_message, new_mutant.get_json())

    def test_is_human(self):
        new_human = self.post_mutant(self.dna_human)
        response_message = {"message": "A human has been added"}
        self.assertEqual(403, new_human.status_code)
        self.assertEqual(response_message, new_human.get_json())

    def test_dna_exist(self):
        self.post_mutant(self.dna_mutant2)
        new_register = self.post_mutant(self.dna_mutant2)
        response_message = {"message": "DNA already exist"}
        self.assertEqual(response_message, new_register.get_json())

    def test_stats_void(self):
        response = self.client.get('/api/stats')
        self.assertEqual(200, response.status_code)

    def tests_stats(self):
        self.post_mutant(self.dna_human)
        self.post_mutant(self.dna_mutant)
        self.post_mutant(self.dna_human2)
        response = self.client.get('/api/stats')
        response_message = {"count_human_dna": 2, "count_mutant_dna": 1, "ratio": 0.5}
        self.assertEqual(200, response.status_code)
        self.assertEqual(response_message, response.get_json())

    def post_mutant(self, dna):
        return self.client.post(
            '/api/mutant',
            data=json.dumps(dna),
            headers={'Content-Type': 'application/json'}
        )
