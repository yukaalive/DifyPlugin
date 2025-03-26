from collections.abc import Generator
from typing import Any, Dict, List
import json
import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import io

class GetChunksTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        # パラメータの取得
        api_key = tool_parameters.get("api_key")
        dataset_id = tool_parameters.get("dataset_id")
    
        try:
            headers = {
                "Authorization": f"Bearer {api_key}"
            }
            
            # 処理ルールの設定
            process_rule = {
                "indexing_technique": "high_quality",
                "process_rule": {
                    "rules": {
                        "pre_processing_rules": [
                            {"id": "remove_extra_spaces", "enabled": True},
                            {"id": "remove_urls_emails", "enabled": True}
                        ],
                        "segmentation": {
                            "separator": "\n\n\n",
                            "max_tokens": 4000
                        }
                    },
                    "mode": "custom"
                }
            }
            
            uploaded_files = {
            'images': [],
            'files': [],
            'pdf_files': [],
            'other_files': []
            }
            for message in context.messages:
                if isinstance(message['content'], dict):
                    file_type = message['content'].get('type')
                    file_url = message['content'].get('url')
                    
                    if file_url:
                        if file_type == 'image':
                            uploaded_files['images'].append(file_url)
                        elif file_type == 'file':
                            file_name = message['content'].get('name', '').lower()
                            mime_type = message['content'].get('mime_type', '').lower()
                            
                            if file_name.endswith('.txt') or 'text/plain' in mime_type:
                                uploaded_files['files'].append(file_url)
                            elif file_name.endswith('.pdf') or 'application/pdf' in mime_type:
                                uploaded_files['pdf_files'].append(file_url)
                            else:
                                uploaded_files['other_files'].append(file_url)
                        # エンドポイント
                        endpoint = f"http://localhost/v1/datasets/{dataset_id}/documents/create-by-file"
            
            # ファイルの取得
            files = self.get_user_files(tool_parameters)
            
            if not files:
                yield self.create_text_message("アップロードされたファイルが見つかりません。")
                return
            
            # データの準備
            data = {
                'data': json.dumps(process_rule)
            }
            
            # ファイルの準備
            files_data = {}
            for i, file in enumerate(files):
                files_data[f'file_{i}'] = (file['filename'], file['content'], file['mime_type'])
            
            # POSTリクエスト送信
            response = requests.post(
                endpoint, 
                headers=headers, 
                data=data, 
                files=files_data, 
                timeout=60
            )
            
            # レスポンス
            if response.status_code >= 400:
                error_msg = f"APIエラー: ステータスコード {response.status_code}"
                try:
                    error_detail = response.json()
                    error_msg += f"\n詳細: {error_detail.get('message', 'Unknown error')}"
                    yield self.create_text_message(error_msg)
                    yield self.create_json_message(error_detail)
                except ValueError:
                    error_msg += f"\nレスポンス: {response.text[:300]}..."
                    yield self.create_text_message(error_msg)
                return
            
            # 成功レスポンス
            result = response.json()
            yield self.create_text_message("ファイルのアップロードに成功しました。")
            yield self.create_json_message(result)

        except Exception as e:
            error_msg = f"処理中にエラーが発生しました: {str(e)}"
            yield self.create_text_message(error_msg)
    
    def get_user_files(self, tool_parameters: dict[str, Any]) -> List[Dict[str, Any]]:

        files = tool_parameters.get("files", [])
        
        if not files and '_files' in tool_parameters:
            files = tool_parameters.get("_files", [])
            
        return files