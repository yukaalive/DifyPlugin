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
        api_key = tool_parameters.get("api_key")
        dataset_id = tool_parameters.get("dataset_id")
        document_id = tool_parameters.get("document_id")
        content = tool_parameters.get("content")
        answer = tool_parameters.get("answer", "")
        keywords = tool_parameters.get("keywords", "")
        
        # 必須パラメータのチェック
        if not api_key:
            yield self.create_text_message("❌ エラー: APIキーが指定されていません")
            return
        
        if not dataset_id:
            yield self.create_text_message("❌ エラー: Dataset ID が指定されていません")
            return
        
        if not document_id:
            yield self.create_text_message("❌ エラー: Document ID が指定されていません")
            return
        
        if not content:
            yield self.create_text_message("❌ エラー: Content が指定されていません")
            return
        
        # キーワードリストを処理
        keyword_list = []
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(",") if k.strip()]
        
        # リクエストヘッダー
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # セグメントデータの準備
        segment_data = {
            "content": content
        }
        
        # オプションのパラメータを追加
        if answer:
            segment_data["answer"] = answer
        
        if keyword_list:
            segment_data["keywords"] = keyword_list
        
        # リクエストデータ構造
        data = {
            "segments": [segment_data]
        }
        
        # プログレス表示
        yield self.create_text_message("🔄 チャンクを追加中...")
        
        try:
            # Dify APIにチャンクを追加するリクエスト
            endpoint = f"https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments"
            
            response = requests.post(
                endpoint,
                headers=headers,
                json=data,
                timeout=30
            )
            
            # レスポンスのステータスコードを確認
            if response.status_code >= 400:
                error_msg = f"❌ APIエラー: ステータスコード {response.status_code}"
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
                yield self.create_text_message(f"✅ チャンクが正常に追加されました!")
                
                # チャンクIDなどの情報を表示
                segment_info = ""
                if "data" in result and "segments" in result["data"]:
                    for i, segment in enumerate(result["data"]["segments"]):
                        segment_info += f"\nチャンク {i+1} ID: {segment.get('id', 'Unknown')}"
                
                if segment_info:
                    yield self.create_text_message(segment_info)
                
                # 詳細情報をJSONとして返す
                yield self.create_json_message(result)
            except ValueError:
                yield self.create_text_message("⚠️ チャンクは追加されましたが、JSONレスポンスの解析に失敗しました")
            
        except requests.Timeout:
            yield self.create_text_message("❌ エラー: APIリクエストがタイムアウトしました。サーバーの応答時間が長いか、ネットワーク接続に問題がある可能性があります。")
        
        except requests.ConnectionError:
            yield self.create_text_message("❌ エラー: APIサーバーへの接続に失敗しました。サーバーURLが正しいか、ネットワーク接続を確認してください。")
            
        except requests.RequestException as e:
            yield self.create_text_message(f"❌ エラー: チャンクの追加に失敗しました: {str(e)}")
            
            if hasattr(e, 'response') and e.response:
                try:
                    error_detail = e.response.json()
                    yield self.create_json_message(error_detail)
                except ValueError:
                    yield self.create_text_message(f"エラーレスポンス: {e.response.text[:300]}...")
        
        except Exception as e:
            yield self.create_text_message(f"❌ 予期しないエラーが発生しました: {str(e)}")