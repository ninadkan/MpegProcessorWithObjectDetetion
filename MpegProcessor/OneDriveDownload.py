# code extracted from https://github.com/pranabdas/Access-OneDrive-via-Microsoft-Graph-Python

# requirements
import requests
import json
import urllib
import os
from getpass import getpass
import time
from datetime import datetime

client_id = os.getenv('CLIENTID')
client_secret= os.getenv('CLIENTSECRET')


URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'

permissions = ['files.readwrite']
response_type = 'token'
redirect_uri = 'http://localhost:8080/'
scope = ''
for items in range(len(permissions)):
    scope = scope + permissions[items]
    if items < len(permissions)-1:
        scope = scope + '+'

print('Click over this link ' + URL + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri)) 

# if you want that login should be prompted everytime, following should be enabled
# print('Click over this link ' + URL + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
#      '&redirect_uri=' + urllib.parse.quote(redirect_uri) + '&prompt=login') 

print('')
print('Sign in to your account, copy the whole redirected URL.')
code = input("Paste the URL here :")
token = code[(code.find('access_token') + len('access_token') + 1) : (code.find('&token_type'))]

# Access One Drive
HEADERS = {'Authorization': 'Bearer ' + token}

def AccessOneDrive(additionalURL, HEADERS):

    URL = 'https://graph.microsoft.com/v1.0/'
    
    response = requests.get(URL + additionalURL, headers = HEADERS)
    if (response.status_code == 200):
        response = json.loads(response.text)
        print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
            '\nConnection valid for one hour. Reauthenticate if required.')
        print ('-------------------------------------------------')
        items = json.loads(requests.get(URL+additionalURL + '/root/children', headers=HEADERS).text)
        items = items['value']
        for entries in range(len(items)):
            print(items[entries]['name'], '| item-id >', items[entries]['id'])
        print ('-------------------------------------------------')
    elif (response.status_code == 401):
        response = json.loads(response.text)
        print('API Error! : ', response['error']['code'],\
            '\nSee response for more details.')
    else:
        response = json.loads(response.text)
        print('Unknown error! See response for more details.')
    
    return

additionalURL = 'me/drive/'
AccessOneDrive(additionalURL,HEADERS)

#Get code
URL_AUTHORIZE = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'

permissions = ['files.ReadWrite.All', 'files.readwrite', 'User.Read']
response_type = 'code'
redirect_uri = 'http://localhost:8080/'
scope = ''
for items in range(len(permissions)):
    scope = scope + permissions[items]
    if items < len(permissions)-1:
        scope = scope + '+'

print('Click over this link ' + URL_AUTHORIZE + '?client_id=' + client_id + '&scope=' + scope + '&response_type=' + response_type+\
     '&redirect_uri=' + urllib.parse.quote(redirect_uri))
print ('')
print('Sign in to your account, copy the whole redirected URL.')
# code = getpass("Paste the URL here :")
print('')
code = input ("Paste the URL here : ")

code = code[(code.find('?code') + len('?code') + 1) :]
print('code = ' + code)

# Now getting the authorization_code
URL_TOKEN = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

data = {
    "client_id": client_id,
    "scope": permissions,
    "code": code,
    "redirect_uri": redirect_uri,
    "grant_type": 'authorization_code',
    "client_secret": client_secret
}
response = requests.post(URL_TOKEN, data=data)

# Following approach does not work!!!
# response = requests.post(URL_TOKEN + '?client_id=' + client_id + '&scope=' + scope + '&grant_type=authorization_code' +\
#      '&redirect_uri=' + urllib.parse.quote(redirect_uri)+ '&code=' + code)

token = ''
# refresh_token=''

if (response.status_code == 200):
    # response = requests.post(URL_TOKEN, data=data)
    json_data = json.loads(response.text)
    json_formatted_str = json.dumps(json_data, indent=2)
    print(json_formatted_str)

    token = json.loads(response.text)["access_token"]
    # Response does not return refresh_token!!!
    # refresh_token = json.loads(response.text)["refresh_token"]
elif (response.status_code == 401):
    response = json.loads(response.text)
    print('API Error! : ', response['error']['code'],\
         '\nSee response for more details.')
else:
    #response = json.loads(response.text)
    print('Unknown error! See response for more details.')
    print ('===========================================')
    print (response.text)
    print ('===========================================')


# Get token
# data = {
#     "client_id": client_id,
#     "scope": permissions,
#     "code": code,
#     "redirect_uri": redirect_uri,
#     "grant_type": 'authorization_code',
#     "client_secret": client_secret
# }
# response = requests.post(URL_TOKEN + '?client_id=' + client_id + '&scope=' + scope + '&grant_type=authorization_code' +\
#      '&redirect_uri=' + urllib.parse.quote(redirect_uri)+ '&code=' + code + '&client_secret=' + client_secret)

# if (response.status_code == 200):
#     # response = requests.post(URL_TOKEN, data=data)
#     json_data = json.loads(response.text)
#     json_formatted_str = json.dumps(json_data, indent=2)
#     print(json_formatted_str)

#     token = json.loads(response.text)["access_token"]
#     print ('token = ' + token)
#     refresh_token = json.loads(response.text)["refresh_token"]
#     print('refresh_token =' + refresh_token)

# elif (response.status_code == 401):
#     response = json.loads(response.text)
#     print('API Error! : ', response['error']['code'],\
#          '\nSee response for more details.')
# else:
#     #response = json.loads(response.text)
#     print('Unknown error! See response for more details.')
#     print ('===========================================')
#     print (response.text)
#     print ('===========================================')


# Refresh token
#This thing is not provided by .... !!!
# def get_refresh_token(refresh_token):

#     data = {
#         "client_id": client_id,
#         "scope": permissions,
#         "refresh_token": refresh_token,
#         "redirect_uri": redirect_uri,
#         "grant_type": 'refresh_token',
#         "client_secret": client_secret,
#     }

#     # response = requests.post(URL_TOKEN, data=data)

#     # response = requests.post(URL_TOKEN + '?client_id=' + client_id + '&scope=' + scope + '&grant_type=refresh_token' +\
#     #  '&redirect_uri=' + urllib.parse.quote(redirect_uri)+ '&refresh_token=' + refresh_token + '&client_secret=' + client_secret)

#     json_data = json.loads(response.text)
#     json_formatted_str = json.dumps(json_data, indent=2)
#     print(json_formatted_str)
  

    

#     token = json.loads(response.text)["access_token"]
#     refresh_token = json.loads(response.text)["refresh_token"]
#     last_updated = time.mktime(datetime.today().timetuple())

#     return token, refresh_token, last_updated

# token, refresh_token, last_updated = get_refresh_token(refresh_token)
# elapsed_time = time.mktime(datetime.today().timetuple()) - last_updated

# if (elapsed_time < 45*60*60):
#     do_something()
# else if (elapsed_time < 59*60*60):
#     token, refresh_token, last_updated = get_refresh_token()
# else:
#     go_to_code_flow()


# One Drive Operations
URL = 'https://graph.microsoft.com/v1.0/'
HEADERS = {'Authorization': 'Bearer ' + token}

# response = requests.get(URL + 'me/drive/', headers = HEADERS)
# if (response.status_code == 200):
#     response = json.loads(response.text)
#     print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
#          '\nConnection valid for one hour. Refresh token if required.')
# elif (response.status_code == 401):
#     response = json.loads(response.text)
#     print('API Error! : ', response['error']['code'],\
#          '\nSee response for more details.')
# else:
#     response = json.loads(response.text)
#     print('Unknown error! See response for more details.')

# def dumpItems(url, HEADERS):
#     items = json.loads(requests.get(url, headers=HEADERS).text)
#     items = items['value']
#     for entries in range(len(items)):
#         print(items[entries]['name'], '| item-id >', items[entries]['id'])
#     return 

# dumpItems(URL + 'me/drive/', HEADERS)

def dumpItemsWithChildren(tempUrl, id):
    
    url = tempUrl + id + '/children'
    items = json.loads(requests.get(url, headers=HEADERS).text)
    items = items['value']
    for entries in range(len(items)):
        print(items[entries]['name'], '| item-id >', items[entries]['id'])
        print ('================-----------------===================')
        newID = items[entries]['id']
        print ('New ID = ' + newID)
        dumpItemsWithChildren(tempUrl,newID )
        print ('================-----------------===================')
    return

tempUrl = URL + 'me/drive/items/'
id = 'E28C89B8D007DF8A!292526'
dumpItemsWithChildren(tempUrl, id)

# id = 'E28C89B8D007DF8A!292542' # Vulcan Drive and Switzerland 2009
id = 'E28C89B8D007DF8A!292529' # Cassette1
def downloadChildren(tempURL, id):
    print("==============  Downloading Images ===========================")
    url = tempUrl + id + '/children'
    items = json.loads(requests.get(url, headers=HEADERS).text)
    items = items['value']
    for entries in range(len(items)):
        print(items[entries]['name'], '| item-id >', items[entries]['id'])
        # Download the file
        # PATH_TO_FILE = '/VHS2PC/Vulcan Drive and Switzerland 2009/'
        PATH_TO_FILE = '/VHS2PC/Casette1/'
        response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root:' +
                                PATH_TO_FILE + items[entries]['name'] + ':/content', headers=HEADERS)

        if (response.status_code == 200):
            filename = "./Data/" + items[entries]['name']
            with open (filename, "wb") as f:
                f.write(response.content)

        elif (response.status_code == 401):
            response = json.loads(response.text)
            print('API Error! : ', response['error']['code'],\
                 '\nSee response for more details.')
        else:
            print('Unknown error! See next response for more details.')
            print (response.text)


        
    return

downloadChildren(tempUrl, id)

