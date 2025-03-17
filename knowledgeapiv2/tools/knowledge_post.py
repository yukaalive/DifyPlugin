from collections.abc import Generator
from typing import Any
import requests
import json

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class KnowledgePostTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータの取得
        action = tool_parameters.get('action')
        dataset_id = tool_parameters.get('datasetId')
        content = tool_parameters.get('content')
        document_id = tool_parameters.get('document_id', '')
        
        # APIキーの取得
        api_key = self.runtime.credentials.get('api_key')
        
        # パラメータのバリデーション
        if not dataset_id:
            yield self.create_text_message("Error: Dataset ID is required")
            return
            
        if not action:
            yield self.create_text_message("Error: Action type is required")
            return
            
        if action in ['create', 'update'] and not content:
            yield self.create_text_message(f"Error: Content is required for {action} action")
            return
            
        if action in ['update', 'delete'] and not document_id:
            yield self.create_text_message(f"Error: Document ID is required for {action} action")
            return
        
        # リクエストURLの構築
        base_url = f"https://api.dify.ai/v1/datasets/{dataset_id}/documents"
        
        # ヘッダー
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = None
            
            if action == 'create':
                # ドキュメント作成
                data = {
                    'content': content,
                    'metadata': {}
                }
                response = requests.post(base_url, json=data, headers=headers)
                
            elif action == 'update':
                # ドキュメント更新
                url = f"{base_url}/{document_id}"
                data = {
                    'content': content,
                    'metadata': {}
                }
                response = requests.put(url, json=data, headers=headers)
                
            elif action == 'delete':
                # ドキュメント削除
                url = f"{base_url}/{document_id}"
                response = requests.delete(url, headers=headers)
                
            else:
                yield self.create_text_message(f"Error: Unsupported action type: {action}")
                return
            
            # レスポンスの処理
            response.raise_for_status()
            result = response.json()
            
            # 結果を返す
            yield self.create_json_message(result)
            
            # 操作結果の要約
            if action == 'create':
                summary = "Successfully created new document"
            elif action == 'update':
                summary = f"Successfully updated document {document_id}"
            elif action == 'delete':
                summary = f"Successfully deleted document {document_id}"
                
            yield self.create_text_message(summary)
            
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")