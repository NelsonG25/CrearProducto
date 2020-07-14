import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
import uuid
 
#CreacionProducto
USER_POOL_ID = 'us-east-1_76vsh1h9d'
CLIENT_ID = '410gjl16ib8k5v1cbvfc2op9vj'
CLIENT_SECRET = '1k1epffssa0ku6ju15pqd9ldf302ckgj1m1smjiokrh6b1uio8h0'

client = None

def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2
    
def initiate_auth(username, password):
    client = boto3.client('cognito-idp',region_name='us-east-1')
    #print(client)
    secret_hash = get_secret_hash(username)
    #print('desde Login_user')
    #print(username)
    #print(password)
    try:
        resp = client.initiate_auth(
                 #UserPoolId=USER_POOL_ID,
                 ClientId=CLIENT_ID,
                 #AuthFlow='ADMIN_USER_PASSWORD_AUTH',
                 AuthFlow='USER_PASSWORD_AUTH',
                 #AuthFlow='ADMIN_NO_SRP_AUTH',
                 AuthParameters={
                     'USERNAME': username,
                     'SECRET_HASH': secret_hash,
                     'PASSWORD': password,
                  },
                ClientMetadata={
                  'username': username,
                  'password': password,
              })
    except client.exceptions.NotAuthorizedException:
        return None, "The username or password is incorrect"
    except client.exceptions.UserNotConfirmedException:
        return None, "User is not confirmed"
    except Exception as e:
        return None, e._str_()
    return resp, None


def lambda_handler(username,password):
    global client
    if client == None:
        client = boto3.client('cognito-idp')
    
    #print(event)
    #body = event
    #username = body['username']
    #password = body['password']
    
    resp, msg = initiate_auth(username, password)
    
    if msg != None:
        return {'message': msg, 
              "error": True, "success": False, "data": None}
    
    if resp.get("AuthenticationResult"):
        return {'message': "success", 
                "error": False, 
                "success": True, 
                "data": {
                "id_token": resp["AuthenticationResult"]["IdToken"],
                "refresh_token": resp["AuthenticationResult"]["RefreshToken"],
                "access_token": resp["AuthenticationResult"]["AccessToken"],
                "expires_in": resp["AuthenticationResult"]["ExpiresIn"],
                "token_type": resp["AuthenticationResult"]["TokenType"]
                }}
    else: #this code block is relevant only when MFA is enabled
        return {"error": True, 
                "success": False, 
                "data": None, "message": None}



                #pip3 install boto3