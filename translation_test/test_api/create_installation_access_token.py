import requests

def create_installation_access_token(jwt_token):
    # 設定情報
    hostname = "https://HOSTNAME"  # GitHub の API ホスト (通常は https://api.github.com)
    installation_id = "INSTALLATION_ID"  # インストール ID

    # API エンドポイント
    url = f"{hostname}/api/v3/app/installations/{installation_id}/access_tokens"

    # HTTP ヘッダー
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # POST リクエストを送信
    response = requests.post(url, headers=headers)

    # 結果を表示
    print(response.status_code)  # ステータスコード (200, 401, 403 など)
    print(response.json())  # JSON レスポンスを取得