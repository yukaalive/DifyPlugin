from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class KnowledgeListTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータの取得
        list_type = tool_parameters.get('type', 'datasets')
        dataset_id = tool_parameters.get('datasetId')
        page = tool_parameters.get('page', 1)
        limit = tool_parameters.get('limit', 20)
        
        # APIキーの取得
        api_key = self.runtime.credentials.get('api_key')
        
        # URLの構築
        if list_type == 'datasets':
            url = "https://api.dify.ai/v1/datasets"
        elif list_type == 'segments':
            if not dataset_id:
                yield self.create_text_message("Error: Dataset ID is required when listing segments")
                return
            url = f"https://api.dify.ai/v1/datasets/{dataset_id}/segments"
        else:
            yield self.create_text_message(f"Error: Unsupported list type: {list_type}")
            return
        
        # リクエストパラメータ
        params = {
            'page': page,
            'limit': limit
        }
        
        # ヘッダー
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            # APIリクエスト実行
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # 結果を返す
            yield self.create_json_message(result)
            
            # 人間が読みやすい要約も提供
            if list_type == 'datasets':
                summary = f"Found {len(result.get('data', {}).get('items', []))} datasets"
            else:
                summary = f"Found {len(result.get('data', {}).get('items', []))} segments for dataset {dataset_id}"
                
            yield self.create_text_message(summary)
            
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")