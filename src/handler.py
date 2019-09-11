import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def mermaidLogger(event, context):
    data = json.loads(event['body'])
    log_level = 'debug'
    if 'level' in data:
        log_level = data.pop('level')
    
    _logger = logger.debug
    if log_level == 'error':
        _logger = logger.error
    elif log_level == 'warn':
        _logger = logger.warn
    
    _logger(data)
    return {
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({'message': 'success'})
    }
