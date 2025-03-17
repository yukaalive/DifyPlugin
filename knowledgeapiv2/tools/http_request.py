from collections.abc import Generator
from typing import Any
import requests
import json

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class HttpRequestTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータの取得
        url = tool_parameters.get('url')
        method = tool_parameters.get('method', 'GET')
        headers_str = tool_parameters.get('headers', '{}')
        body = tool_parameters.get('body', '')
        
        # パラメータのバリデーション
        if not url:
            yield self.create_text_message("Error: URL is required")
            return
        
        # ヘッダーのパース
        try:
            headers = json.loads(headers_str) if headers_str else {}
        except json.JSONDecodeError:
            yield self.create_text_message("Error: Headers must be valid JSON")
            return
        
        # リクエストの実行
        try:
            # リクエストオプションの設定
            request_kwargs = {
                'url': url,
                'headers': headers,
                'timeout': 30  # デフォルトタイムアウト
            }
            
            # POSTやPUTなどのメソッドの場合、ボディを追加
            if method in ['POST', 'PUT', 'PATCH'] and body:
                # Content-Typeに応じてボディの形式を調整
                content_type = headers.get('Content-Type', '').lower()
                if 'application/json' in content_type:
                    try:
                        request_kwargs['json'] = json.loads(body)
                    except json.JSONDecodeError:
                        yield self.create_text_message("Error: Body must be valid JSON for Content-Type: application/json")
                        return
                else:
                    request_kwargs['data'] = body
            
            # リクエスト実行
            response = requests.request(method, **request_kwargs)
            
            # レスポンス情報の準備
            result = {
                'status': response.status_code,
                'headers': dict(response.headers)
            }
            
            # レスポンスボディの処理
            try:
                result['data'] = response.json()
            except json.JSONDecodeError:
                result['data'] = response.text
            
            # 結果を返す
            yield self.create_json_message(result)
            
            # 人間が読みやすい要約も提供
            summary = f"HTTP {method} request to {url} completed with status {response.status_code}"
            yield self.create_text_message(summary)
            
        except requests.RequestException as e:
            yield self.create_text_message(f"Request error: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"Error: {str(e)}")