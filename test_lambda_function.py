import unittest
import json

from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def test_lambda_function(self):

        event = {}
        context = {}

        response = lambda_handler(event, context)

        # Check response code equal to 200
        self.assertEqual(response['statusCode'], 200)

        # Verify string message body
        response_body = json.loads(response['body'])
        self.assertIsInstance(response_body['message'], str)

if __name__ == "__main__":

    unittest.main()