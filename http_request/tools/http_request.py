import json
from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class HTTPRequestTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # URLを取得（必須パラメータ）
        url = tool_parameters.get("url", "")
        
        # URLの検証
        if not url.startswith("http://") and not url.startswith("https://"):
            yield self.create_text_message("エラー: URLはhttp://またはhttps://で始まる必要があります。")
            return
            
        # リクエストタイプを取得（デフォルトはGET）
        request_type = tool_parameters.get("request_type", "GET")
        
        # 送信データの取得（POSTの場合）
        data_to_send = None
        data_str = tool_parameters.get("data_to_send", "")
        
        # POSTでデータがある場合、JSONとして処理
        if request_type == "POST" and data_str:
            try:
                data_to_send = json.loads(data_str)
            except json.JSONDecodeError:
                yield self.create_text_message("エラー: 送信データは正しいJSON形式である必要があります。例: {\"名前\": \"値\"}")
                return
        
        try:
            # リクエスト時にわかりやすいユーザーエージェントを設定
            headers = {
                "User-Agent": "Dify-Simple-API-Request-Tool/1.0"
            }
            
            # リクエスト送信
            if request_type == "GET":
                response = requests.get(url, headers=headers, timeout=30)
            else:  # POST
                response = requests.post(url, json=data_to_send, headers=headers, timeout=30)
            
            # レスポンスコードの確認
            if response.status_code >= 400:
                yield self.create_text_message(f"エラー: リクエストに失敗しました。エラーコード: {response.status_code}\n理由: {response.reason}")
                return
                
            # レスポンスの解析と返却
            content_type = response.headers.get("Content-Type", "")
            
            # JSONの場合は整形して返却
            if "application/json" in content_type:
                try:
                    result = response.json()
                    # JSONを読みやすく整形
                    if isinstance(result, dict) or isinstance(result, list):
                        # シンプルな文字列として返す（初心者向け）
                        yield self.create_text_message("APIからのレスポンス（JSON）:\n" + json.dumps(result, indent=2, ensure_ascii=False))
                        # 必要に応じて構造化データも返す（高度な処理用）
                        yield self.create_json_message(result)
                    else:
                        yield self.create_text_message(f"APIからのレスポンス: {result}")
                except json.JSONDecodeError:
                    # JSON解析に失敗した場合は普通のテキストとして返す
                    yield self.create_text_message("APIからのレスポンス（テキスト）:\n" + response.text)
            else:
                # 通常のテキストとして返す
                yield self.create_text_message("APIからのレスポンス（テキスト）:\n" + response.text)
            
        except requests.exceptions.ConnectionError:
            yield self.create_text_message("エラー: 接続できませんでした。URLが正しいか確認してください。")
        except requests.exceptions.Timeout:
            yield self.create_text_message("エラー: リクエストがタイムアウトしました。もう一度お試しください。")
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"エラー: リクエストに問題がありました。{str(e)}")