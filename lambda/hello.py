import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    status_code = {
        'statusCode': 200
    }
    headers = {
        'headers': {
            'Content-Type': 'text/plain'
        }
    }
    body = {
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }

    response = {
        **status_code,
        **headers,
        **body
    }

    return response
