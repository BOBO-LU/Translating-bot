#print out all the language code used by the translator

import os, requests, uuid, json


os.environ['TRANSLATOR_TEXT_ENDPOINT'] = str('https://api.cognitive.microsofttranslator.com/')

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

path = '/languages?api-version=3.0'
constructed_url = endpoint + path

headers = {
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

request = requests.get(constructed_url, headers=headers)
response = request.json()
response_json = json.dumps(response["translation"], sort_keys=True, indent=2,
                 ensure_ascii=False, separators=(',', ': '))
print(response_json)