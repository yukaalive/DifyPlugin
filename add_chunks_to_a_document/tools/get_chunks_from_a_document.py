from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetChunksTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Get chunks from a Dify document
        """
        # パラメータを取得
        api_key = tool_parameters.get("api_key")
        dataset_id = tool_parameters.get("dataset_id")
        document_id = tool_parameters.get("document_id")
        keyword = tool_parameters.get("keyword", "")
        status = tool_parameters.get("status", "")
        
        # リクエストヘッダーの定義
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # クエリパラメータの準備
        params = {}
        if keyword:
            params["keyword"] = keyword
        if status:
            params["status"] = status
    
        # Dify APIからチャンクを取得するリクエスト
        endpoint = f"http://localhost/v1/datasets/{dataset_id}/documents/{document_id}/segments"
        
        response = requests.get(
            endpoint,
            headers=headers,
            params=params,
            timeout=60
        )
        
        # レスポンスのステータスコードを確認
        if response.status_code >= 400:
            error_msg = f"APIエラー: ステータスコード {response.status_code}"
            try:
                error_detail = response.json()
                error_msg += f"\n詳細: {error_detail.get('message', 'Unknown error')}"
                yield self.create_json_message(error_detail)
            except ValueError:
                error_msg += f"\nレスポンス: {response.text[:300]}..."
            
            yield self.create_text_message(error_msg)
            return
        
        # 成功レスポンス

        result = response.json()
        segments_data = []
        total_segments = 0


        segments_data = result["data"]
        total_segments = len(segments_data)
        
        # 概要情報を表示
        summary = f"ドキュメントから {total_segments} 個のチャンクを取得しました"
        yield self.create_text_message(summary)
        
        # 変数として各セグメント情報を出力
        yield self.create_variable_message("segments", segments_data)
        yield self.create_variable_message("total_segments", total_segments)
        
        # セグメントIDとコンテンツのリストを作成
        segment_ids = [s.get("id", "") for s in segments_data]
        segment_contents = [s.get("content", "") for s in segments_data]
        
        yield self.create_variable_message("segment_ids", segment_ids)
        yield self.create_variable_message("segment_contents", segment_contents)
        

        for i, segment in enumerate(segments_data[:10]):
            yield self.create_variable_message(f"segment_{i+1}", segment)

        yield self.create_json_message(result)
