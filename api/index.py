import json

def handler(request):
    if request['method'] == 'POST':
        body = json.loads(request['body'])
        message = body.get('message', 'hi')
        return {
            'statusCode': 200,
            'body': json.dumps({'response': f'You said: {message}. Hello!'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps({'response': 'API ready!'})
    }
