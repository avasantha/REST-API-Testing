import requests
import json

from pprint import pprint
import os
dirname = os.path.dirname(__file__)
filename = os.path.realpath("{0}/callhub.json".format(dirname))
api_key="d2a23df41486edd77c7d7a58c1746df4dbed7036"
headers = {"Authorization": "Token %s" % api_key}

def create_phonebook(phonebook_name):
    print('*****Creating PhoneBook*****')
    url = "https://api.callhub.io/v1/phonebooks/"
    file = open(filename,'r')
    request_json = json.loads(file.read())
    response=requests.post(url,data=request_json[phonebook_name],headers = headers)
    pprint(response.status_code)
    return int(json.loads(response.text)['id'])

def add_contacts(phonebook_id,contact):
    print('*****Adding Contact to PhoneBook*****')
    url="https://api.callhub.io/v1/phonebooks/%d/create_contact/" % phonebook_id
    file = open(filename,'r')
    req_json=json.loads(file.read())
    response=requests.post(url,data=req_json[contact],headers = headers)
    pprint(response.json())
    pprint(response.status_code)
    return int(json.loads(response.text)['contact']['id'])

def add_tag(tag_name):
    print('*****Creating Tag *****')
    url = 'https://api.callhub.io/v2/tags/'
    tag_data = {"tag": tag_name}
    tag_response = requests.post(url, data = tag_data, headers=headers)
    pprint(tag_response.status_code)
    return str(tag_response.json()["id"])

def updateTagToContact(contact_id,tag_id):
    print('*****Adding Tag to Contact*****')
    contact_url = 'https://api.callhub.io/v2/contacts/%d/taggings/' % contact_id
    contact_data = {"tags": [tag_id]}
    contact_response = requests.patch(contact_url, data = contact_data, headers=headers)
    pprint(contact_response.status_code)

phonebook_id = create_phonebook('phonebook')
contact1_id = add_contacts(phonebook_id,'John')
contact2_id =add_contacts(phonebook_id,'Michael')
tag_id = add_tag("Testing")
updateTagToContact(contact1_id,tag_id)