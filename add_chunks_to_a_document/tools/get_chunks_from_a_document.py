from collections.abc import Generator
from typing import Any, Dict, List

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
        
        try:
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
            
            # レスポンスを整理
            processed_data = self._parse_response(result)

            
            # 変数として各セグメント情報を出力
            yield self.create_variable_message("segments", processed_data["segments"])
            yield self.create_variable_message("segment_ids", processed_data["segment_ids"])
            yield self.create_variable_message("segment_contents", processed_data["segment_contents"])
            
            # 個別のセグメント情報を出力
            for i, segment in enumerate(processed_data["segments"][:30]):
                yield self.create_variable_message(f"segment_{i+1}", segment)
            yield self.create_json_message(processed_data)
            
        except Exception as e:
            error_msg = f"エラーが発生しました: {str(e)}"
            yield self.create_text_message(error_msg)
    
    def _parse_response(self, response: dict) -> dict:
        """
        APIレスポンスを整理
        
        :param response: APIから返されたJSONレスポンス
        :return: 整理されたデータ辞書
        """
        result = {}
        
        # セグメントデータを取得
        segments_data = response.get("data", [])
        
        # セグメントIDとコンテンツのリストを作成
        segment_ids = [s.get("id", "") for s in segments_data]
        segment_contents = [s.get("content", "") for s in segments_data]
        
        # 必要なデータを結果辞書に格納
        result["segments"] = segments_data
        result["segment_ids"] = segment_ids
        result["segment_contents"] = segment_contents
        
        return result