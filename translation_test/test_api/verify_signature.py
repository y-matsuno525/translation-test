import hashlib
import hmac
from django.core.exceptions import PermissionDenied #参考：https://docs.djangoproject.com/ja/5.1/ref/exceptions/

#GitHubから送られてきた署名を検証
def verify_signature(payload_body, webhook_secret, signature_header):

    if not signature_header:
        #raiseは例外を発生させるために使う
        #tryの中でverify_signatureを実行してraiseで返されるとexceptが実行される
        raise PermissionDenied("x-hub-signature-256ヘッダーが存在しません。") 
    
    #以下はまだ詳しくわからないが、検証処理のコア部分
    hash_object = hmac.new(webhook_secret.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()

    if not hmac.compare_digest(expected_signature, signature_header):
        raise PermissionDenied("署名が一致しません。")
    
    return 
    