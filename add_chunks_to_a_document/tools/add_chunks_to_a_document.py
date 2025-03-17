from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class AddChunkTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Add a chunk to a Dify dataset
        """
        # パラメータを取得
        dataset_id = tool_parameters.get("dataset_id")
        document_id = tool_parameters.get("document_id")
        content = tool_parameters.get("content")
        answer = tool_parameters.get("answer", "")
        keywords = tool_parameters.get("keywords", "")
        
        # 必須パラメータのチェック
        if not dataset_id:
            yield self.create_text_message("Dataset ID is required")
            return
        
        if not document_id:
            yield self.create_text_message("Document ID is required")
            return
        
        if not content:
            yield self.create_text_message("Content is required")
            return
        
        # APIキーを認証情報から取得
        api_key = self.runtime.credentials["api_key"]
        
        # キーワードリストを処理
        keyword_list = []
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
        
        # リクエストヘッダー
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # リクエストデータ
        data = {
            "dataset_id": dataset_id,
            "document_id": document_id,
            "content": content
        }
        
        # オプションのパラメータを追加
        if answer:
            data["answer"] = answer
        
        if keyword_list:
            data["keywords"] = keyword_list
        
        try:
            # Dify APIにチャンクを追加するリクエスト
            response = requests.post(
                f"https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments", 
                headers=headers,
                json=data,
                timeout=30
            )
            
            response.raise_for_status()
            
            # 成功レスポンス
            result = response.json()
            yield self.create_text_message(f"チャンクが正常に追加されました。\nチャンクID: {result.get('id', 'Unknown')}")
            
            # デバッグ情報も返す
            yield self.create_json_message(result)
            
        except requests.RequestException as e:
            # エラーメッセージ
            yield self.create_text_message(f"チャンクの追加に失敗しました: {str(e)}")
            
            if hasattr(e, 'response') and e.response:
                try:
                    error_detail = e.response.json()
                    yield self.create_json_message(error_detail)
                except ValueError:
                    yield self.create_text_message(f"エラーレスポンス: {e.response.text}")