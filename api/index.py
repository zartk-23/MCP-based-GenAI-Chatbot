import json

def handler(event, context=None):
    if event.get('httpMethod') == 'POST':
        try:
            body = json.loads(event['body'])
            message = body.get('message', '').strip().lower()
            if not message:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'No message'})
                }
            if 'hi' in message or 'hello' in message:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'response': 'Hello! I am your AI. Ask me anything!'})
                }
            elif 'weather' in message:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'response': 'It’s sunny in London! ☀️'})
                }
            else:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'response': f'You said: {message}'})
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'response': 'API is LIVE! Send POST with {"message": "hi"}'})
        }
