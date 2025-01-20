from api import app
from aws_lambda_wsgi import handler

# Wrap Flask app with WSGI interface
def lambda_handler(event, context):
    return handler(app, event, context)
