import base64
import jwt
import hashlib
import requests
from Crypto.PublicKey import RSA
import time
import json

# Create Checksum
def create_checksum(http_method, raw_url, headers, request_body):
        string_to_hash = http_method.upper() + '|' + raw_url.lower() + '|' + headers + '|' + request_body    
        base64_string = base64.b64encode(hashlib.sha256(str.encode(string_to_hash)).digest()).decode('utf-8')
        return base64_string   

# Create security token
def create_jwt_token(appication_id, api_key, http_method, raw_url, headers, request_body,
                     iat=time.time(), algorithm='HS256', version='V1'):
    checksum = create_checksum(http_method, raw_url, headers, request_body)
    payload = {'appid': appication_id,
               'iat': iat,
               'version': version,
               'checksum': checksum}
    token = jwt.encode(payload, api_key, algorithm=algorithm).decode('utf-8')
    return token




