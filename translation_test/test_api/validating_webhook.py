import hashlib
import hmac
from django.core.exceptions import PermissionDenied #参考：https://docs.djangoproject.com/ja/5.1/ref/exceptions/

def verify_signature(payload_body, secret_token, signature_header):
    """
    GitHubから送信されたWebhookの署名を検証する関数

    引数:
        payload_body: リクエストボディ（例: request.body）
        secret_token: GitHub AppのWebhookシークレット
        signature_header: GitHubから受け取った x-hub-signature-256 ヘッダーの値

    署名が不正な場合、PermissionDenied例外を発生させる
    """
    if not signature_header:
        #raiseは例外を発生させるために使う
        #tryの中でverify_signatureを実行してraiseで返されるとexceptが実行される
        raise PermissionDenied("x-hub-signature-256ヘッダーが存在しません。") 
    
    #以下はまだ詳しくわからないが、検証処理のコア部分
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()

    if not hmac.compare_digest(expected_signature, signature_header):
        raise PermissionDenied("署名が一致しません。")
    