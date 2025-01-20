import json

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))

    message = 'Hello from Lambda!'

    return {
        'statusCode': 200,
        'body': json.dumps({ 'message': message })
    }