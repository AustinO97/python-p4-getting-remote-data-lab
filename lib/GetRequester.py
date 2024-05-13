import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    # def get_response_body(self):
    #     search_term = 'Daniel'

    #     search_term_formatted = search_term.replace(' ', '+')
    #     fields = ['name', 'occupation']
    #     fields_formatted = ','.join(fields)
    #     limit = 1

    #     URL = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json?name={search_term_formatted}&fields={fields_formatted}&limit={limit}'

    #     response = requests.get(URL)
    #     return response.content

    # def load_json(self):
    #     search_term = 'Daniel'

    #     search_term_formatted = search_term.replace(' ', '+')
    #     fields = ['name', 'occupation']
    #     fields_formatted = ','.join(fields)
    #     limit = 1

    #     URL = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json?name={search_term_formatted}&fields={fields_formatted}&limit={limit}'

    #     response = requests.get(URL).json()      
    #     return response
    
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())
    
# results_json = GetRequester().load_json()
# print(json.dumps(results_json, indent=1))