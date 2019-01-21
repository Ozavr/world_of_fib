from settings import INPUT_CONFINES


fib_input_schema = {
    'type': 'object',
    'properties': {
        'from': {
            'type': 'number', 
            'minimum': INPUT_CONFINES['from']['min'], 
            'maximum': INPUT_CONFINES['from']['max']
        },
        'to': {
            'type': 'number',
            'minimum': INPUT_CONFINES['to']['min'], 
            'maximum': INPUT_CONFINES['to']['max']
        }
    },
    'required': ['from', 'to']
}

