# code extracted from https://github.com/pranabdas/Access-OneDrive-via-Microsoft-Graph-Python

# requirements
import requests
import json
import urllib
import os
from getpass import getpass
import time
from datetime import datetime



URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
client_id = "362422eb-d9d6-4245-9eca-2be5cf256450"
permissions = ['files.readwrite']
response_type = 'token'
redirect_uri = 'http://localhost:8080/'
scope = ''
for items in range(len(permissions)):
    scope = scope + permissions[items]
    if items < len(permissions)-1:
        scope = scope + '+'

print('Click over this link ' +URL + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri))
print('Sign in to your account, copy the whole redirected URL.')
code = input("Paste the URL here :")
token = code[(code.find('access_token') + len('access_token') + 1) : (code.find('&token_type'))]
URL = 'https://graph.microsoft.com/v1.0/'
HEADERS = {'Authorization': 'Bearer ' + token}
response = requests.get(URL + 'me/drive/', headers = HEADERS)
if (response.status_code == 200):
    response = json.loads(response.text)
    print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
         '\nConnection valid for one hour. Reauthenticate if required.')
elif (response.status_code == 401):
    response = json.loads(response.text)
    print('API Error! : ', response['error']['code'],\
         '\nSee response for more details.')
else:
    response = json.loads(response.text)
    print('Unknown error! See response for more details.')



# Get code
URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
client_id = "362422eb-d9d6-4245-9eca-2be5cf256450"
permissions = ['offline_access', 'files.readwrite', 'User.Read']
response_type = 'code'
redirect_uri = 'http://localhost:8080/'
scope = ''
for items in range(len(permissions)):
    scope = scope + permissions[items]
    if items < len(permissions)-1:
        scope = scope + '+'

print('Click over this link ' +URL + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri))
print('Sign in to your account, copy the whole redirected URL.')
code = getpass("Paste the URL here :")
code = code[(code.find('?code') + len('?code') + 1) :]

URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

response = requests.post(URL + '?client_id=' + client_id + '&scope=' + scope + '&grant_type=authorization_code' +\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri)+ '&code=' + code)



# Get token
data = {
    "client_id": client_id,
    "scope": permissions,
    "code": code,
    "redirect_uri": redirect_uri,
    "grant_type": 'authorization_code',
    "client_secret": client_secret
}

response = requests.post(URL, data=data)

token = json.loads(response.text)["access_token"]
refresh_token = json.loads(response.text)["refresh_token"]


# Refresh token
def get_refresh_token():
    data = {
        "client_id": client_id,
        "scope": permissions,
        "refresh_token": refresh_token,
        "redirect_uri": redirect_uri,
        "grant_type": 'refresh_token',
        "client_secret": 'xxxx-yyyy-zzzz',
    }

    response = requests.post(URL, data=data)

    token = json.loads(response.text)["access_token"]
    refresh_token = json.loads(response.text)["refresh_token"]
    last_updated = time.mktime(datetime.today().timetuple())

    return token, refresh_token, last_updated

token, refresh_token, last_updated = get_refresh_token()


elapsed_time = time.mktime(datetime.today().timetuple()) - last_updated

# if (elapsed_time < 45*60*60):
#     do_something()
# else if (elapsed_time < 59*60*60):
#     token, refresh_token, last_updated = get_refresh_token()
# else:
#     go_to_code_flow()



# One Drive Operations
URL = 'https://graph.microsoft.com/v1.0/'

HEADERS = {'Authorization': 'Bearer ' + token}

response = requests.get(URL + 'me/drive/', headers = HEADERS)
if (response.status_code == 200):
    response = json.loads(response.text)
    print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
         '\nConnection valid for one hour. Refresh token if required.')
elif (response.status_code == 401):
    response = json.loads(response.text)
    print('API Error! : ', response['error']['code'],\
         '\nSee response for more details.')
else:
    response = json.loads(response.text)
    print('Unknown error! See response for more details.')


items = json.loads(requests.get(URL + 'me/drive/root/children', headers=HEADERS).text)
items = items['value']
for entries in range(len(items)):
    print(items[entries]['name'], '| item-id >', items[entries]['id'])

