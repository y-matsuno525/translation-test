import os
from django.http import JsonResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from validating_webhook import verify_signature
from create_jwt import create_jwt
from dotenv import load_dotenv #インストールしたはずなのに



def validate_webhook(request):

    #.envファイルのパスを指定して読み込む
    load_dotenv('.env')
    secret_token = os.getenv('WEBHOOK_SECRET')

    #リクエストヘッダーからx-hub-signature-256を取得
    signature_header = request.META.get("HTTP_X_HUB_SIGNATURE_256")

    try:
        #署名検証を実施
        verify_signature(request.body, secret_token, signature_header)
    except PermissionDenied as e:
        return HttpResponseForbidden(str(e))
    
    return render(request, "test_api/validate_webhook.html")

def create_jwt(request):
    jwt = create_jwt()
    return render(request, "test_api/create_jwt.html")

