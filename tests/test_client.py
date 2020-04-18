import unittest

from datosgobmx.client import api, create_query_parts, create_url, make_call

class TestClient(unittest.TestCase):
    def test_create_url(self):
        """Tests that URL's are created correctly"""

        # Default url
        result_url = create_url()
        expected_url = 'https://api.datos.gob.mx/v2/api-catalog'
        self.assertEqual(expected_url, result_url)

        # Custom endpoint without query
        result_url = create_url('SOME-OTHER-ENDPOINT')
        expected_url = 'https://api.datos.gob.mx/v2/SOME-OTHER-ENDPOINT'
        self.assertEqual(expected_url, result_url)

        # Endpoint with equal query
        result_url = create_url('SOME-OTHER', query={'page': 1})
        expected_url = 'https://api.datos.gob.mx/v2/SOME-OTHER?page=1'
        self.assertEqual(expected_url, result_url)

        # Endpoint with range query
        result_url = create_url('SOME-OTHER', query={'score>=': 1})
        expected_url = 'https://api.datos.gob.mx/v2/SOME-OTHER?score>=1'
        self.assertEqual(expected_url, result_url)

        result_url = create_url('SOME-OTHER', query={
            'score<=': 1, 'score>=': 11
        })
        expected_url = 'https://api.datos.gob.mx/v2/SOME-OTHER?score<=1&score>=11'
        self.assertEqual(expected_url, result_url)


    def test_create_query_parts(self):
        """Tests that the user query dict is converted correctly to query parts
        """
        # Equality - default and explicit
        query = {
            "pageSize": "10",
            "parametro=": "PM2.5",
            "estacionesid": 300
        }
        result_parts = create_query_parts(query)
        expected_parts = ['pageSize=10', 'parametro=PM2.5', 'estacionesid=300']
        self.assertEqual(expected_parts, result_parts)

        # Ranges
        query = {
            "date-insert>=": "2017-06-29T19:00:00",
            "date-insert<=": "2017-07-29T19:00:00"
        }
        result_parts = create_query_parts(query)
        expected_parts = [
            'date-insert>=2017-06-29T19%3A00%3A00', 
            'date-insert<=2017-07-29T19%3A00%3A00'
        ]
        self.assertEqual(expected_parts, result_parts)


if __name__ == '__main__':
    unittest.main()