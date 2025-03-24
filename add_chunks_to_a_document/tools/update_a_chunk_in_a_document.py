from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class UpdateChunkTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        """
        Update a chunk in a Dify dataset
        """
        # パラメータを取得
        api_key = tool_parameters.get("api_key")
        dataset_id = tool_parameters.get("dataset_id")
        document_id = tool_parameters.get("document_id")
        segment_id = tool_parameters.get("segment_id")
        content = tool_parameters.get("content")
        answer = tool_parameters.get("answer", "")
        keywords = tool_parameters.get("keywords", "")
        enabled = tool_parameters.get("enabled", True)
        regenerate_child_chunks = tool_parameters.get("regenerate_child_chunks", False)
        
        # keywordをカンマで区切りしてリストにする
        keyword_list = []
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
        
        # リクエストヘッダーの定義
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # API仕様に合わせてリクエストデータ構造を修正
        segment_data = {
            "content": content
        }
        
        # オプションのパラメータを追加
        if answer:
            segment_data["answer"] = answer
        
        if keyword_list:
            segment_data["keywords"] = keyword_list
            
        # enabledパラメータを追加
        segment_data["enabled"] = enabled
        
        # リクエストデータ構造
        data = {
            "segment": segment_data
        }
        
        # regenerate_child_chunksがTrueの場合は追加
        if regenerate_child_chunks:
            data["regenerate_child_chunks"] = True
        
        try:
            # Dify APIにチャンクを更新リクエスト
            # API仕様に合わせてエンドポイントを修正
            base_url = tool_parameters.get("base_url", "http://localhost")
            endpoint = f"{base_url}/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"
            
            response = requests.post(
                endpoint,
                headers=headers,
                json=data,
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
            try:
                result = response.json()
                yield self.create_text_message(f"チャンクが正常にアップデートされました")
                
                # 詳細情報をJSONで返却
                yield self.create_json_message(result)
            except ValueError:
                yield self.create_text_message("チャンクは更新されましたが、JSONレスポンスの解析に失敗しました")
            
        except requests.Timeout:
            yield self.create_text_message("エラー: APIリクエストがタイムアウトしました。サーバーの応答時間が長いか、ネットワーク接続に問題がある可能性があります。")
        
        except requests.ConnectionError:
            yield self.create_text_message("エラー: APIサーバーへの接続に失敗しました。サーバーURLが正しいか、ネットワーク接続を確認してください。")
            
        except requests.RequestException as e:
            yield self.create_text_message(f"エラー: チャンクの更新に失敗しました: {str(e)}")
            
            if hasattr(e, 'response') and e.response:
                try:
                    error_detail = e.response.json()
                    yield self.create_json_message(error_detail)
                except ValueError:
                    yield self.create_text_message(f"エラーレスポンス: {e.response.text[:300]}...")