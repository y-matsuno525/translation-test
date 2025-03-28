import requests

def create_installation_access_token(jwt):
    # 設定情報
    hostname = "https://api.github.com"
    installation_id = "61373723"

    # API エンドポイント
    url = f"{hostname}/api/v3/app/installations/{installation_id}/access_tokens"

    # HTTP ヘッダー
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    #POSTリクエストを送信
    response = requests.post(url, headers=headers)

    return response.json()