from typing import Any
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
import requests

class KnowledgeAPIProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # APIキーの検証
        api_key = credentials.get("api_key")
        if not api_key:
            raise ToolProviderCredentialValidationError("API Key is required")
        
        # 試験的なリクエストを送信して検証
        try:
            # データセット一覧を取得してみる
            url = "https://api.dify.ai/v1/datasets"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            raise ToolProviderCredentialValidationError(f"Failed to validate API Key: {str(e)}")