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
        
        try:
            # Dify APIからチャンクを取得するリクエスト
            endpoint = f"http://localhost/v1/datasets/{dataset_id}/documents/{document_id}/segments"
            
            response = requests.get(
                endpoint,
                headers=headers,
                params=params,
                timeout=30
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
                total_segments = 0
                segments_data = []
                
                if "data" in result and "segments" in result["data"]:
                    segments = result["data"]["segments"]
                    total_segments = len(segments)
                    
                    # 整形したセグメントデータを作成
                    for segment in segments:
                        segment_info = {
                            "id": segment.get("id", ""),
                            "content": segment.get("content", ""),
                            "answer": segment.get("answer", ""),
                            "keywords": segment.get("keywords", []),
                            "enabled": segment.get("enabled", True)
                        }
                        segments_data.append(segment_info)
                
                # 概要情報を表示
                summary = f"ドキュメントから {total_segments} 個のチャンクを取得しました"
                yield self.create_text_message(summary)
                
                # 変数として各セグメント情報を出力
                yield self.create_variable_message("segments", segments_data)
                yield self.create_variable_message("total_segments", total_segments)
                yield self.create_variable_message("segment_ids", [s.get("id", "") for s in segments_data])
                yield self.create_variable_message("segment_contents", [s.get("content", "") for s in segments_data])
                
                # 個別の変数としても各チャンクを出力（単一チャンクや先頭・末尾チャンク用）
                if total_segments > 0:
                    yield self.create_variable_message("first_segment", segments_data[0])
                    yield self.create_variable_message("last_segment", segments_data[-1])
                    
                    # 各チャンクを個別の変数としても出力（最大10個まで）
                    for i, segment in enumerate(segments_data[:10]):
                        yield self.create_variable_message(f"segment_{i+1}", segment)
                
                # 完全なレスポンスをJSONとしても出力
                yield self.create_json_message(result)
                
            except ValueError:
                yield self.create_text_message("チャンクデータの取得に成功しましたが、JSONレスポンスの解析に失敗しました")
            
        except requests.Timeout:
            yield self.create_text_message("エラー: APIリクエストがタイムアウトしました。サーバーの応答時間が長いか、ネットワーク接続に問題がある可能性があります。")
        
        except requests.ConnectionError:
            yield self.create_text_message("エラー: APIサーバーへの接続に失敗しました。サーバーURLが正しいか、ネットワーク接続を確認してください。")
            
        except requests.RequestException as e:
            yield self.create_text_message(f"エラー: チャンクの取得に失敗しました: {str(e)}")
            
            if hasattr(e, 'response') and e.response:
                try:
                    error_detail = e.response.json()
                    yield self.create_json_message(error_detail)
                except ValueError:
                    yield self.create_text_message(f"エラーレスポンス: {e.response.text[:300]}...")