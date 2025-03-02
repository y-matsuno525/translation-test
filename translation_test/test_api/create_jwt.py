from jwt import JWT, jwk_from_pem
import time
import sys


def create_jwt():

    #GitHubAppのAppIDを設定
    app_id = "1152089"

    #Private keyを開く

    with open("private_key.pem", 'rb') as pem_file:
        try:
            signing_key = jwk_from_pem(pem_file.read())
        except FileNotFoundError as err:
            print(err)

    payload = {
        #発行時刻
        'iat': int(time.time()),
        #有効期限が切れるタイミング
        'exp': int(time.time()) + 600,
        
        # GitHubAppのAppID
        'iss': app_id
    }

    #JWTを作成
    jwt_instance = JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

    return encoded_jwt