import os
from django.http import JsonResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from translation_test.test_api.verify_signature import verify_signature
from create_jwt import create_jwt
from create_installation_access_token import create_installation_access_token
from dotenv import load_dotenv 


#認証認可フェーズ
def authentication_and_authorization(request):

    #.envファイルのパスを指定して読み込む
    load_dotenv('.env')
    webhook_secret = os.getenv('WEBHOOK_SECRET')

    #リクエストヘッダーからx-hub-signature-256を取得
    signature_header = request.META.get("HTTP_X_HUB_SIGNATURE_256")

    try:
        #署名検証を実施
        verify_signature(request.body, webhook_secret, signature_header)
    except PermissionDenied as e:
        return HttpResponseForbidden(str(e))
    
    jwt = create_jwt()

    installation_access_token = create_installation_access_token(jwt)

    return render(request, "test_api/create_jwt.html")

