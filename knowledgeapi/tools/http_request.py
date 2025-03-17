import json
from collections.abc import Generator
from typing import Any, Dict, Optional

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class HttpRequestTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # モードを取得
        mode = tool_parameters.get("mode", "http")
        
        if mode == "http":
            # カスタムHTTPリクエストモード
            yield from self._handle_http_request(tool_parameters)
        elif mode == "dify_kb":
            # Difyナレッジベースモード
            yield from self._handle_dify_knowledge_base(tool_parameters)
        else:
            yield self.create_text_message(f"エラー: 不明なモード '{mode}' が指定されました。'http'または'dify_kb'を指定してください。")
    
    # カスタムHTTPリクエスト処理
    def _handle_http_request(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータを取得
        url = tool_parameters.get("url", "")
        method = tool_parameters.get("method", "GET")
        headers_str = tool_parameters.get("headers", "")
        body_str = tool_parameters.get("body", "")
        
        # URLの検証
        if not url:
            yield self.create_text_message("エラー: URLが指定されていません")
            return
            
        if not (url.startswith("http://") or url.startswith("https://")):
            yield self.create_text_message("エラー: URLはhttp://またはhttps://で始まる必要があります")
            return
        
        # ヘッダーの解析
        headers = {}
        if headers_str:
            try:
                headers = json.loads(headers_str)
                if not isinstance(headers, dict):
                    yield self.create_text_message("エラー: ヘッダーは正しいJSON形式のオブジェクトである必要があります")
                    return
            except json.JSONDecodeError:
                yield self.create_text_message("エラー: ヘッダーは有効なJSON形式である必要があります")
                return
                
        # ボディの解析
        body = None
        if body_str and method != "GET" and method != "HEAD":
            try:
                body = json.loads(body_str)
            except json.JSONDecodeError:
                yield self.create_text_message("エラー: ボディは有効なJSON形式である必要があります")
                return
        
        # リクエスト実行
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=body,
                timeout=30
            )
            
            # レスポンスの整形
            result = {
                "url": url,
                "method": method,
                "status_code": response.status_code,
                "status_text": response.reason,
                "headers": dict(response.headers),
                "content_type": response.headers.get("Content-Type", ""),
            }
            
            # レスポンスの内容を分析
            content_type = response.headers.get("Content-Type", "").lower()
            
            # レスポンス本文を追加
            if "application/json" in content_type:
                try:
                    result["body"] = response.json()
                    # 読みやすいテキスト表示用
                    formatted_json = json.dumps(response.json(), indent=2, ensure_ascii=False)
                except json.JSONDecodeError:
                    result["body"] = response.text
                    formatted_json = response.text
            else:
                result["body"] = response.text
                formatted_json = response.text
            
            # 人間が読みやすい形式で結果を表示
            formatted_result = f"【HTTPリクエスト結果】\n\n"
            formatted_result += f"📡 リクエスト: {method} {url}\n"
            formatted_result += f"🔢 ステータスコード: {response.status_code} {response.reason}\n"
            
            # ヘッダーの主要項目を表示
            formatted_result += f"📋 レスポンスヘッダー:\n"
            for key in ["Content-Type", "Content-Length", "Server", "Date"]:
                if key in response.headers:
                    formatted_result += f"  - {key}: {response.headers[key]}\n"
            
            # レスポンスボディの抜粋（長すぎる場合は省略）
            formatted_result += f"\n📄 レスポンスボディ:\n"
            if len(formatted_json) > 1500:
                formatted_result += formatted_json[:1500] + "...\n(レスポンスが長いため省略されました。完全なレスポンスはJSONレスポンスを参照してください。)"
            else:
                formatted_result += formatted_json
            
            # 人間が読みやすい結果とJSONデータの両方を返す
            yield self.create_text_message(formatted_result)
            yield self.create_json_message(result)
            
        except requests.exceptions.ConnectionError:
            yield self.create_text_message("エラー: 接続できませんでした。URLが正しいか確認してください。")
        except requests.exceptions.Timeout:
            yield self.create_text_message("エラー: リクエストがタイムアウトしました（30秒）。サーバーの負荷を確認してください。")
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"エラー: リクエスト中に問題が発生しました: {str(e)}")
        except Exception as e:
            yield self.create_text_message(f"予期しないエラーが発生しました: {str(e)}")
    
    # Difyナレッジベース処理
    def _handle_dify_knowledge_base(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータを取得
        operation = tool_parameters.get('operation', 'list_datasets')
        dataset_id = tool_parameters.get('dataset_id', '')
        document_id = tool_parameters.get('document_id', '')
        query = tool_parameters.get('query', '')
        result_count = tool_parameters.get('result_count', '5')
        api_key = tool_parameters.get('api_key', '')
        
        # APIキーの検証
        if not api_key:
            yield self.create_text_message("エラー: Dify APIキーが指定されていません")
            return
            
        if not (api_key.startswith('app-') or api_key.startswith('sk-')):
            yield self.create_text_message("エラー: DifyのAPIキーはapp-またはsk-で始まる必要があります")
            return
        
        # 操作の種類に応じた処理を行う
        if operation == 'list_datasets':
            result = self._list_datasets(api_key)
        elif operation == 'get_dataset_info':
            result = self._get_dataset_info(api_key, dataset_id)
        elif operation == 'list_documents':
            result = self._list_documents(api_key, dataset_id)
        elif operation == 'get_segments':
            result = self._get_document_segments(api_key, dataset_id, document_id)
        elif operation == 'search':
            result = self._search_dataset(api_key, dataset_id, query, result_count)
        else:
            yield self.create_text_message(f"エラー: 不明な操作です: {operation}")
            return
            
        # エラーチェック
        if 'error' in result:
            yield self.create_text_message(f"エラー: {result['error']}")
            if 'detail' in result:
                yield self.create_text_message(f"詳細: {result['detail']}")
            return
            
        # 操作結果を返す
        if 'formatted_result' in result:
            yield self.create_text_message(result['formatted_result'])
        
        # JSON結果も返す（高度な処理用）
        if 'json_result' in result:
            yield self.create_json_message(result['json_result'])
    
    # Dify APIリクエスト用の共通関数
    def _make_dify_request(self, api_key: str, endpoint: str, method: str = 'GET', 
                           params: Optional[Dict[str, Any]] = None, 
                           json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        base_url = 'https://api.dify.ai/v1'
        url = f"{base_url}{endpoint}"
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=30)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, params=params, json=json_data, timeout=30)
            else:
                return {'error': f'サポートされていないメソッド: {method}'}
            
            # エラー処理
            if response.status_code >= 400:
                return {
                    'error': f'APIエラー (ステータスコード: {response.status_code})',
                    'detail': response.text
                }
                
            return response.json()
            
        except requests.RequestException as e:
            return {'error': f'リクエストエラー: {str(e)}'}
        except ValueError:
            return {'error': 'JSONパースエラー: レスポンスの形式が無効です'}
    
    # 以下、各操作の実装
    
    # ナレッジベース一覧取得
    def _list_datasets(self, api_key: str) -> Dict[str, Any]:
        result = self._make_dify_request(api_key, '/datasets')
        
        if 'error' in result:
            return result
            
        # 結果を整形して返す
        if 'data' in result and isinstance(result['data'], list):
            datasets = result['data']
            
            if len(datasets) == 0:
                return {'formatted_result': "ナレッジベースが見つかりませんでした。Difyで新しいナレッジベースを作成してください。"}
                
            # 結果を整形
            formatted_result = "【ナレッジベース一覧】\n\n"
            for dataset in datasets:
                formatted_result += f"📚 {dataset.get('name', '名称なし')}\n"
                formatted_result += f"  ID: {dataset.get('id', '')}\n"
                formatted_result += f"  説明: {dataset.get('description', '説明なし')}\n"
                formatted_result += f"  ドキュメント数: {dataset.get('document_count', 0)}\n"
                formatted_result += f"  作成日: {dataset.get('created_at', '')}\n\n"
                
            return {
                'formatted_result': formatted_result,
                'json_result': result
            }
        else:
            return {'error': "ナレッジベース情報の取得に失敗しました。レスポンス形式が予期しないものでした。"}
    
    # ナレッジベース情報取得
    def _get_dataset_info(self, api_key: str, dataset_id: str) -> Dict[str, Any]:
        if not dataset_id:
            return {'error': "ナレッジベースIDが指定されていません"}
            
        result = self._make_dify_request(api_key, f'/datasets/{dataset_id}')
        
        if 'error' in result:
            return result
            
        # 結果を整形して返す
        dataset = result.get('data', {})
        if dataset:
            formatted_result = "【ナレッジベース詳細情報】\n\n"
            formatted_result += f"📚 {dataset.get('name', '名称なし')}\n"
            formatted_result += f"  ID: {dataset.get('id', '')}\n"
            formatted_result += f"  説明: {dataset.get('description', '説明なし')}\n"
            formatted_result += f"  作成日: {dataset.get('created_at', '')}\n"
            formatted_result += f"  更新日: {dataset.get('updated_at', '')}\n"
            formatted_result += f"  ドキュメント数: {dataset.get('document_count', 0)}\n"
            formatted_result += f"  セグメント数: {dataset.get('word_count', 0)}\n"
            formatted_result += f"  データベースタイプ: {dataset.get('indexing_technique', '')}\n"
            
            return {
                'formatted_result': formatted_result,
                'json_result': result
            }
        else:
            return {'error': "ナレッジベース情報の取得に失敗しました。指定されたIDのナレッジベースが存在しない可能性があります。"}
    
    # ドキュメント一覧取得
    def _list_documents(self, api_key: str, dataset_id: str) -> Dict[str, Any]:
        if not dataset_id:
            return {'error': "ナレッジベースIDが指定されていません"}
            
        result = self._make_dify_request(api_key, f'/datasets/{dataset_id}/documents')
        
        if 'error' in result:
            return result
            
        # 結果を整形して返す
        if 'data' in result and isinstance(result['data'], list):
            documents = result['data']
            
            if len(documents) == 0:
                return {'formatted_result': "このナレッジベースにはドキュメントがありません。Difyでドキュメントをアップロードしてください。"}
                
            # 結果を整形
            formatted_result = "【ドキュメント一覧】\n\n"
            for doc in documents:
                formatted_result += f"📄 {doc.get('name', 'ドキュメント名なし')}\n"
                formatted_result += f"  ID: {doc.get('id', '')}\n"
                formatted_result += f"  タイプ: {doc.get('document_type', 'タイプなし')}\n"
                formatted_result += f"  サイズ: {doc.get('size', 0)} バイト\n"
                formatted_result += f"  作成日: {doc.get('created_at', '')}\n\n"
                
            return {
                'formatted_result': formatted_result,
                'json_result': result
            }
        else:
            return {'error': "ドキュメント情報の取得に失敗しました。レスポンス形式が予期しないものでした。"}
    
    # ドキュメントセグメント取得
    def _get_document_segments(self, api_key: str, dataset_id: str, document_id: str) -> Dict[str, Any]:
        if not dataset_id:
            return {'error': "ナレッジベースIDが指定されていません"}
            
        if not document_id:
            return {'error': "ドキュメントIDが指定されていません"}
            
        result = self._make_dify_request(api_key, f'/datasets/{dataset_id}/documents/{document_id}/segments')
        
        if 'error' in result:
            return result
            
        # 結果を整形して返す
        if 'data' in result and isinstance(result['data'], list):
            segments = result['data']
            
            if len(segments) == 0:
                return {'formatted_result': "このドキュメントにはセグメントがありません。"}
                
            # 結果を整形
            formatted_result = "【ドキュメント内容】\n\n"
            for i, segment in enumerate(segments, 1):
                formatted_result += f"セグメント {i}:\n"
                formatted_result += f"{segment.get('content', '内容なし')}\n\n"
                
            return {
                'formatted_result': formatted_result,
                'json_result': result
            }
        else:
            return {'error': "セグメント情報の取得に失敗しました。レスポンス形式が予期しないものでした。"}
    
    # ナレッジベース検索
    def _search_dataset(self, api_key: str, dataset_id: str, query: str, result_count: str) -> Dict[str, Any]:
        if not dataset_id:
            return {'error': "ナレッジベースIDが指定されていません"}
            
        if not query:
            return {'error': "検索クエリが指定されていません"}
            
        # 整数に変換
        try:
            top_k_int = int(result_count)
        except (ValueError, TypeError):
            top_k_int = 5
            
        # 検索リクエストを実行
        json_data = {
            "query": query,
            "top_k": top_k_int
        }
        
        result = self._make_