import requests
import json

# r = requests.get('http://127.0.0.1:8000/contacts.json')
# contact_list = json.loads(r.text)

r = requests.post('http://127.0.0.1:8000/contacts/17.json', data = {'method':'DELETE'})

print(r.text)
# print(contact_list)
