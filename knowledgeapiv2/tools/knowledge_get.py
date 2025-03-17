from collections.abc import Generator
from typing import Any
import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class KnowledgeGetTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータの取得
        dataset_id = tool_parameters.get('datasetId')
        segment_id = tool_parameters.get('segmentId')
        query = tool_parameters.get('query')
        retrieval_type = tool_parameters.get('retrieval_type', 'semantic')
        limit = tool_parameters.get('limit', 10)
        
        # APIキーの取得
        api_key = self.runtime.credentials.get('api_key')
        
        # パラメータのバリデーション
        if not dataset_id:
            yield self.create_text_message("Error: Dataset ID is required")
            return
            
        if not query:
            yield self.create_text_message("Error: Search query is required")
            return
        
        # リクエストURLとパラメータの構築
        url = f"https://api.dify.ai/v1/datasets/{dataset_id}/search"
        
        params = {
            'query': query,
            'limit': int(limit),
            'retrieval_type': retrieval_type
        }
        
        # セグメントIDが指定されている場合は追加
        if segment_id:
            params['segment_id'] = segment_id
        
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
            search_results = result.get('data', {}).get('items', [])
            summary = f"Found {len(search_results)} results for query: '{query}'"
            
            if len(search_results) > 0:
                top_result = search_results[0].get('text', 'No content')[:100] + "..."
                summary += f"\nTop result: {top_result}"
                
            yield self.create_text_message(summary)
            
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")