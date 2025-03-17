from typing import Any

import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class DifyChunkAdderProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """
        Validate the API key by making a simple API call to Dify
        """
        api_key = credentials.get("api_key")
        
        if not api_key:
            raise ToolProviderCredentialValidationError("API key is required")
        
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            response = requests.get(
                "https://api.dify.ai/v1",  # 実際のエンドポイントに変更
                headers=headers,
                timeout=10
            )
            
            if response.status_code != 200:
                raise ToolProviderCredentialValidationError(f"Invalid API key: {response.text}")
        
        except requests.RequestException as e:
            raise ToolProviderCredentialValidationError(f"Failed to validate API key: {str(e)}")