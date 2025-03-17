# Difyのプラグインの機能紹介

## プラグインとは
プラグインとは、開発者がより手軽に機能を拡張できる、サードパーティ製の拡張モジュールです。Difyプラットフォームには、Difyチームやコミュニティによってメンテナンスされた多くのツールがすでに用意されていますが、多様化するニッチなニーズを完全に満たせない場合があります。また、新しいツールをDifyプラットフォームに開発・統合するには、時間と手間がかかることが少なくありません。

そこで、よりアジャイルな開発を可能にするため、Difyのエコシステムをオープンにし、包括的なプラグイン開発SDKを提供することにしました。これにより、すべての開発者が独自のツールを容易に構築し、サードパーティのモデルやツールをシームレスに統合して、アプリケーションの可能性を飛躍的に向上させることができます。

## プラグインのメリット
新しいプラグインシステムは、従来のフレームワークの制約を超え、より豊富で強力な拡張機能を提供します。明確に定義されたシナリオに対応するために、5つの異なるプラグインタイプを用意しており、開発者はDifyアプリケーションを自由にカスタマイズし、強化することができます。

さらに、プラグインシステムは共有しやすいように設計されています。Difyマーケットプレイス、GitHub、またはローカルファイルパッケージを通じてプラグインを配布できます。他の開発者は、これらのプラグインを迅速にインストールし、そのメリットを享受できます。

Difyマーケットプレイスは、開発者向けのオープンなエコシステムであり、モデル、ツール、AIエージェント、拡張機能、プラグインバンドルなど、幅広いリソースを提供しています。マーケットプレイスを通じて、サードパーティのサービスを既存のDifyアプリケーションにシームレスに統合し、機能を強化し、Difyコミュニティ全体の発展に貢献できます。

新しいモデルを統合したい場合も、Difyの既存機能を拡張するための専用ツールを追加したい場合も、Dify マーケットプレイスには必要なリソースが揃っています。より多くの開発者の皆様に参加していただき、Difyのエコシステムを共に発展させ、関係者全員に利益をもたらすことを願っています。


## プラグインの種類
### モデル
これらのプラグインは、さまざまなAIモデル（主要なLLMプロバイダーやカスタムモデルを含む）を統合し、LLM APIの設定とリクエストを処理します。モデルプラグインの作成の詳細については、クイックスタート：モデルプラグインをご覧ください。

### ツール
ツールとは、Chatflow、Workflow、Agentタイプのアプリケーションから呼び出すことができるサードパーティのサービスのことです。Difyアプリケーションの機能を拡張するためのAPI実装を提供します。たとえば、Google検索プラグインの開発については、クイックスタート：ツールプラグインをご参照ください。

### エージェント戦略
エージェント戦略プラグインは、エージェントノード内の推論および意思決定ロジックを定義します。これには、ツール選択、呼び出し、および結果処理などが含まれます。

エージェント戦略プラグインは、エージェントノード内部の推論および意思決定ロジックを定義します。これには、ツールの選択、実行、およびLLMから返された結果の処理ロジックが含まれます。詳細な開発ガイダンスについては、クイックスタート：エージェント戦略プラグインをご参照ください。

### 拡張機能
よりシンプルなシナリオのエンドポイント機能のみを提供する軽量プラグインで、HTTPサービスを介して迅速な拡張を可能にします。基本的なAPI呼び出しを必要とする簡単な統合に最適です。詳細については、クイックスタート：拡張機能プラグインをご参照ください。

### バンドル

「プラグインバンドル」は、複数のプラグインをまとめたものです。バンドルを使用すると、厳選されたプラグインセットを一度にインストールできます。プラグインを1つずつ追加する手間が省けます。プラグインバンドルの作成の詳細については、プラグイン開発：バンドルプラグインをご覧ください。

## プラグインの新機能
- LLMのマルチモーダル対応を拡張
プラグインを使用すると、LLMがマルチモーダルデータを処理する能力を高めることができます。開発者は、画像編集や動画処理などのタスクを追加できます。トリミングや背景の削除から、ポートレート画像の処理まで、幅広い用途に対応できます。

- 開発者フレンドリーなデバッグ機能
プラグインシステムは、一般的なIDEとデバッグツールをサポートしています。いくつかの環境変数を設定するだけで、SaaSとして実行されているDifyインスタンスにリモートで接続できます。Difyでプラグインに対して実行した操作は、デバッグのためにローカルランタイムに転送されます。

- 永続的なデータストレージ
より複雑なユースケースに対応するために、プラグインシステムにはデータ永続性が組み込まれています。

    -- プラグインレベルのデータストレージ: ワークスペースレベルの情報をプラグインと共有して、より高度なカスタム機能を実現できます。
    -- 組み込みのデータ管理: プラグインはデータを確実に保存および管理できるため、複雑なビジネスロジックを容易に実装できます。

- 便利な双方向通信
プラグインは、Difyのコア機能と双方向に対話できるようになりました。

    -- AIモデルの呼び出し
    -- ツールの使用
    -- アプリケーションへのアクセス
    -- ナレッジベースとの対話
    -- 関数ノードの呼び出し（質問分類、パラメータ抽出など）

この双方向メカニズムにより、プラグインは既存のDify機能を活用するだけでなく、スタンドアロンのゲートウェイとしても機能し、アプリケーションのユースケースを拡大します。

- 強化されたエンドポイントのカスタマイズ機能
既存のDify API（ChatbotやWorkflow APIなど）に加えて、プラグイン内にカスタムAPIを作成できるようになりました。開発者はビジネスロジックをプラグインとしてラップし、Dify マーケットプレイスでホストすることで、データ処理とリクエスト処理のエンドポイントサポートを自動的に得られます。

# プラグイン開発の入門
- はじめに
このガイドでは、ツール型プラグインやモデルプラグインなど、様々な種類のプラグインの開発方法を例を挙げて説明します。これにより、プラグイン開発における様々な機能の組み合わせを迅速に理解し、活用できるようになります。開発を始める前には、まず開発環境を用意し、必要なフレームワークをインストールして初期設定を行ってください。詳細は以下を参照してください：

- 開発環境のセットアップ
GoogleSearchツールを例に、ツール型プラグインの開発方法を紹介します。具体的な手順は以下をご覧ください：

- ツール型プラグイン
AnthropicやXinferenceモデルを例に、事前にトレーニングされたモデルプラグインとカスタムモデルプラグインの開発方法について説明します。

    -- 事前にトレーニングされたモデルは、GPTやClaudeなどの商用モデルを指し、追加の訓練や設定なしで利用できます。
    -- カスタムモデルプラグインは、開発者が独自に訓練または設定したモデルを統合し、特定のニーズに合わせた機能を提供します。

具体的な開発例は以下を参照してください：

- モデル型プラグイン
Extensionプラグインにより、開発者はビジネスロジックをプラグインとしてパッケージ化し、Difyプラットフォーム上でAPIサービスとして公開できます。詳細は以下をご覧ください：

- 拡張機能型プラグイン
インターフェースドキュメント
プラグインの詳細なインターフェース仕様が必要な場合は、以下の標準仕様書を参照してください：

- 一般的な構造の標準定義
- マニフェストの標準定義
- ツールとの接続の標準定義
- モデルとの接続の標準定義
- エンドポイントの標準定義
- 拡張エージェント策略
- Difyサービスの逆呼び出し機能
    -- アプリの逆呼び出し
    -- モデルの逆呼び出し
    -- ノードの逆呼び出し
    -- ツールの逆呼び出し
- プラグインの永続化されたストレージ機能

## ツール型プラグイン
Tool（ツール）プラグインは、チャットフロー、ワークフロー、エージェントといったアプリタイプから参照できる外部ツールであり、Difyアプリの機能を拡張するために使用されます。例えば、アプリにオンライン検索機能や画像生成機能を追加するといったことが可能です。ツールプラグインは、包括的なツールセットとAPI実装機能を提供します。

本篇では、「ツールプラグイン」とは、ツールプロバイダーファイル、機能コード、およびその他の関連コンポーネントを含む、一揃いのプロジェクトを指します。ツールプロバイダーは複数のツール（これは、単一のツールが提供する追加機能と解釈できます）を含むことがあり、以下の構造で構成されます。

- ツールプロバイダー
    - Tool A
    - Tool B

この記事では、GoogleSearchを例に、ツールプラグインを迅速に開発する方法をご紹介します。

### 事前準備
- Dify プラグインの Scaffolding（スキャフォールディング）ツール
- Python 環境 (バージョン 3.12 以上)

プラグイン開発用のScaffoldingツールの準備方法については、初期化開発ツールをご参照ください。

### 新規プロジェクトの作成
Scaffoldingのコマンドラインツールを実行し、新しいDifyプラグインプロジェクトを作成します。

<code>
./dify-plugin-darwin-arm64 plugin init
</code>

バイナリファイルの名前を dify に変更し、/usr/local/bin ディレクトリにコピーした場合は、次のコマンドを実行して新しいプラグインプロジェクトを作成できます。

<code>
dify plugin init
</code>

以下、コマンドラインツール dify を使用します。もし問題が発生した場合は、dify コマンドを、お使いのツールの実行パスに置き換えてください。

### プラグインの種類とテンプレートの選択
プラグインには、ツール、モデル、そしてエクステンションの3種類があります。SDK内のすべてのテンプレートには、完全なコードプロジェクトが付属しています。以下の部分では、ツールプラグインテンプレートを例として使用します。

プラグイン開発に精通されている方は、各種プラグインの実装にあたり、スキーマ仕様をご参照ください。

### プラグイン権限の設定
プラグインを正常に接続するには、Difyプラットフォームの権限を読み取る必要があります。このサンプルツールプラグインには、以下の権限を付与する必要があります。

- ツール
- アプリ
- 永続的ストレージジストレージの有効化、デフォルトサイズのストレージの割り当て
- エンドポイントの登録許可

ターミナルで方向キーを使って権限を選択し、"タグ"のブタンで権限を付与してください。

すべての権限項目にチェックを入れたら、Enterキーを押してプラグインの作成を完了させてください。システムが自動的にプラグインプロジェクトのコードを生成します。

### 開発ツールプラグイン
#### 1. ツールプロバイダーの yaml ファイルを作成する
ツールプロバイダーファイルは、ツールプラグインの基本的な設定ファイルとして機能し、ツールが利用するために必要な認証情報を提供します。このセクションでは、この yaml ファイルの記述方法について説明します。

/provider ディレクトリに移動し、その中にある yaml ファイルの名前を google.yaml に変更します。この yaml ファイルには、プロバイダー名、アイコン、作成者など、ツールプロバイダーに関する情報が含まれます。これらの情報は、プラグインのインストール時に表示されます。

<sample_code>
identity: # ツールプロバイダーの基本情報
  author: Your-name # 作成者
  name: google # 名前。一意である必要があり、他のプロバイダーと重複できません
  label: # ラベル。フロントエンドでの表示に使用
    en_US: Google # 英語ラベル
    zh_Hans: Google # 中国語ラベル
    ja_JP: Google # 日本語ラベル
    pt_BR: Google # プルトガル語ラベル
  description: # 説明。フロントエンドでの表示に使用
    en_US: Google # 英語説明
    zh_Hans: Google # 中国語説明
    ja_JP: : Google # 日本語説明
    pt_BR: : Google # プルトガル語説明
  icon: icon.svg # アイコン。_assets フォルダに配置する必要があります
  tags: # タグ。フロントエンドでの表示に使用
    - search
</sample_code>


identity には、作成者、名前、ラベル、説明、アイコンなど、ツールプロバイダーの基本的な情報が含まれます。

アイコンは添付ファイルとして扱い、プロジェクトのルートディレクトリにある _assets フォルダに配置する必要があります。

タグは、ユーザーがプラグインをカテゴリ別にすばやく検索するのに役立ちます。現在サポートされているすべてのタグは以下のとおりです。

<sample_tag>
class ToolLabelEnum(Enum):
  SEARCH = 'search'
  IMAGE = 'image'
  VIDEOS = 'videos'
  WEATHER = 'weather'
  FINANCE = 'finance'
  DESIGN = 'design'
  TRAVEL = 'travel'
  SOCIAL = 'social'
  NEWS = 'news'
  MEDICAL = 'medical'
  PRODUCTIVITY = 'productivity'
  EDUCATION = 'education'
  BUSINESS = 'business'
  ENTERTAINMENT = 'entertainment'
  UTILITIES = 'utilities'
  OTHER = 'other'
</sample_tag>

ファイルパスが /tools ディレクトリにあることを確認してください。完全なパスは次のようになります。

<path>
plugins:
  tools:
    - "google.yaml"
</path>

ここで、google.yaml ファイルのパスは、プラグインプロジェクト内の絶対パスで指定する必要があります。

##### サードパーティサービスの認証情報を設定する
開発を容易にするため、サードパーティサービスである SerpApi が提供する Google Search API を利用することにしました。SerpApi を使用するには API キーが必要となるため、yaml ファイルに credentials_for_provider フィールドを追加する必要があります。

完全なコードは次のとおりです。

<sample_code>
identity:
  author: Dify
  name: google
  label:
    en_US: Google
    zh_Hans: Google
    ja_JP: Google
    pt_BR: Google
  description:
    en_US: Google
    zh_Hans: GoogleSearch
    ja_JP: Google
    pt_BR: Google
  icon: icon.svg
  tags:
    - search
credentials_for_provider: # credentials_for_provider フィールドを追加
  serpapi_api_key:
    type: secret-input
    required: true
    label:
      en_US: SerpApi API key
      zh_Hans: SerpApi API key
      ja_JP: SerpApi API key
      pt_BR: chave de API SerpApi
    placeholder:
      en_US: Please input your SerpApi API key
      zh_Hans: 请输入你的 SerpApi API key
      ja_JP: SerpApi API keyを入力してください
      pt_BR: Por favor, insira sua chave de API SerpApi
    help:
      en_US: Get your SerpApi API key from SerpApi
      zh_Hans: 从 SerpApi 获取您的 SerpApi API key
      ja_JP: SerpApiからSerpApi APIキーを取得する
      pt_BR: Obtenha sua chave de API SerpApi da SerpApi
    url: https://serpapi.com/manage-api-key
tools:
  - tools/google_search.yaml
extra:
  python:
    source: google.py
</sample_code>

credentials_for_provider の子構造は、ProviderConfig の仕様に準拠する必要があります。

このプロバイダーに含まれるツールを指定する必要があります。この例では、tools/google_search.yaml ファイルが 1 つだけ含まれています。

プロバイダーは、基本情報を定義するだけでなく、コードによるロジックの実装も必要です。そのため、実装ロジックを指定する必要があります。この例では、機能のコードファイルは google.py に配置されていますが、ここではまだ実装せず、先に google_search のコードを作成します。これは、google_search の機能が google.py の実装に依存するためです。

#### 2. ツールの YAML ファイルへの入力
1つのツールベンダーが複数のツールを提供することがあります。各ツールは、その基本的な情報、パラメータ、出力などを記述した yaml ファイルによって定義される必要があります。

ここでは、GoogleSearch ツールを例にとり、/tools フォルダに新しい google_search.yaml ファイルを作成する手順を見ていきましょう。

<sample_code>
identity:
  name: google_search
  author: Dify
  label:
    en_US: GoogleSearch
    zh_Hans: 谷歌搜索
    ja_JP: Google検索
    pt_BR: Pesquisa Google
description:
  human:
    en_US: A tool for performing a Google SERP search and extracting snippets and webpages.Input should be a search query.
    zh_Hans: 一个用于执行 Google SERP 搜索并提取片段和网页的工具。输入应该是一个搜索查询。
    ja_JP: Google SERP 検索を実行し、スニペットと Web ページを抽出するためのツール。入力は検索クエリである必要があります。
    pt_BR: Uma ferramenta para realizar pesquisas no Google SERP e extrair snippets e páginas da web. A entrada deve ser uma consulta de pesquisa.
  llm: A tool for performing a Google SERP search and extracting snippets and webpages.Input should be a search query.
parameters:
  - name: query
    type: string
    required: true
    label:
      en_US: Query string
      zh_Hans: 查询字符串
      ja_JP: クエリ文字列
      pt_BR: Cadeia de consulta
    human_description:
      en_US: used for searching
      zh_Hans: 用于搜索网页内容
      ja_JP: ネットの検索に使用する
      pt_BR: usado para pesquisar
    llm_description: key words for searching
    form: llm
extra:
  python:
    source: tools/google_search.py
</sample_code>

- identity: ツールの名前、作成者、ラベル、説明といった基本的な情報が含まれます。
- parameters: パラメータに関する設定項目です。各項目の詳細は以下の通りです。
    -- name (必須): パラメータ名。一意である必要があり、他のパラメータ名との重複は許容されません。
    -- type (必須): パラメータの型。string (文字列)、number (数値)、boolean (真偽値)、select (選択式ドロップダウン)、secret-input (暗号化入力フィールド) の5種類がサポートされています。機密性の高い情報を取り扱う場合は、必ず secret-input 型を使用してください。
    -- label (必須): パラメータのラベル。フロントエンドに表示される際に用いられます。
    -- form (必須): フォームの種類。llm と form の2種類がサポートされています。
        --- Agentアプリケーションにおいて、llm はパラメータがLLMによって推論されることを意味し、form はツールを使用する前にユーザーが設定できるパラメータを意味します。
        --- ワークフローアプリケーションにおいては、llm と form の両方のパラメータに対してフロントエンドでの入力が求められます。ただし、llm パラメータはツールノードの入力変数として機能します。
    -- required: 必須項目であるかどうかを示すフラグです。
        --- llm モードの場合、required が true に設定されたパラメータは、Agentが推論によって値を決定する必要があります。
        --- form モードの場合、required が true に設定されたパラメータは、ユーザーが会話を開始する前にフロントエンドで値を入力する必要があります。
    -- options: パラメータの選択肢。
        --- llm モードでは、Dify はすべての選択肢をLLMに渡し、LLM はこれらの選択肢に基づいて推論を行います。
        --- form モードでは、type が select に設定されている場合、フロントエンドにこれらの選択肢が表示されます。
    -- default: デフォルト値。
    -- min: 最小値。パラメータの型が number の場合に設定可能です。
    -- max: 最大値。パラメータの型が number の場合に設定可能です。
    -- human_description: フロントエンドに表示されるパラメータの説明文です。多言語に対応しています。
    -- placeholder: 入力フィールドに表示されるプレースホルダーテキストです。form 形式で、パラメータの型が string、number、secret-input の場合に設定できます。多言語に対応しています。
    -- llm_description: LLMに渡されるパラメータの説明文です。LLMがパラメータの内容をより深く理解できるよう、できる限り詳細な情報を提供してください。
    
#### 3. ツールコードの準備
ツールの設定情報を入力したら、ツールの機能コードを記述し、ツールのロジックを実装します。 /tools ディレクトリに google_search.py を作成し、以下の内容を記述します。

<sample_code>
from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

SERP_API_URL = "https://serpapi.com/search"

class GoogleSearchTool(Tool):
    def _parse_response(self, response: dict) -> dict:
        result = {}
        if "knowledge_graph" in response:
            result["title"] = response["knowledge_graph"].get("title", "")
            result["description"] = response["knowledge_graph"].get("description", "")
        if "organic_results" in response:
            result["organic_results"] = [
                {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                }
                for item in response["organic_results"]
            ]
        return result

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        params = {
            "api_key": self.runtime.credentials["serpapi_api_key"],
            "q": tool_parameters["query"],
            "engine": "google",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en",
        }

        response = requests.get(url=SERP_API_URL, params=params, timeout=5)
        response.raise_for_status()
        valuable_res = self._parse_response(response.json())
        
        yield self.create_json_message(valuable_res)
</sample_code>

この例では、serpapi にリクエストを送信し、self.create_json_message を使用して json 形式のデータを返しています。その他の戻り値の型については、ツールインターフェースドキュメントを参照してください。

#### 4. ツールプロバイダーコードの作成
最後に、プロバイダーのコードを実装します。これは、プロバイダーの認証情報を検証するために使用されます。認証情報の検証に失敗すると、ToolProviderCredentialValidationError 例外が発生します。検証に成功すると、google_search ツールサービスが正常にリクエストされます。

/provider ディレクトリに google.py ファイルを作成し、以下のコードを記述します。

<sample_code>
from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from tools.google_search import GoogleSearchTool

class GoogleProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            for _ in GoogleSearchTool.from_credentials(credentials).invoke(
                tool_parameters={"query": "test", "result_type": "link"},
            ):
                pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
</sample_code>

### プラグインのデバッグ
プラグインが正常に動作するかテストします。Dify はリモートデバッグをサポートしています。「プラグイン管理」ページで、デバッグキーとリモートサーバーアドレスを取得してください。

プラグインプロジェクトに戻り、.env.example ファイルをコピーして .env にリネームし、取得したリモートサーバーアドレスとデバッグキーを入力します。

<.env_file>
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=localhost
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
</.env_file>

python -m main コマンドを実行してプラグインを起動します。プラグインページで、プラグインがワークスペースにインストールされていることを確認できます。これで、他のチームメンバーもこのプラグインを使用できます。

### プラグインのパッケージ化
プラグインが正常に動作することを確認したら、以下のコマンドラインツールを使用してプラグインをパッケージ化し、名前を付けます。実行後、現在のフォルダに google.difypkg ファイルが作成されます。これがプラグインの最終的なパッケージです。

<code>
dify plugin package ./google
</code>

おめでとうございます。これで、ツールタイプのプラグインの開発、デバッグ、パッケージ化の全プロセスが完了しました。

### プラグインの公開
Dify Plugins コードリポジトリにアップロードして、プラグインを公開しましょう。アップロードする前に、プラグインがプラグイン公開仕様に準拠していることを確認してください。レビューに合格すると、コードはメインブランチにマージされ、Dify Marketplace に自動的に公開されます。

## モデル型プラグイン
モデルタイププラグインを導入することで、Difyプラットフォームは特定のモデルプロバイダーが提供するモデルを利用できるようになります。例えば、OpenAIモデルプラグインをインストールすると、DifyプラットフォームからOpenAIのGPT-4やGPT-4o-2024-05-13といったモデルをリクエストできるようになります。

### モデルプラグインの構造
プラグインモデルの開発に関する理解を深めるために、モデルタイププラグインの構造例を以下に示します。

モデルプロバイダー：OpenAI、Anthropic、Googleなどの大規模モデル開発企業です。

モデルカテゴリ：プロバイダーに応じて、大規模言語モデル（LLM）、テキスト埋め込みモデル、音声テキスト変換モデルなどがあります。

具体的なモデル：claude-3-5-sonnet、gpt-4-turboなど。

プラグインプロジェクトのコード構造：
- モデルプロバイダー
  - モデルカテゴリ
    - 具体的なモデル
    
Anthropicを例にとると、モデルプラグインの構造は次のようになります。

- Anthropic
  - llm
    claude-3-5-sonnet-20240620
    claude-3-haiku-20240307
    claude-3-opus-20240229
    claude-3-sonnet-20240229
    claude-instant-1.2
    claude-instant-1

OpenAIを例にとると、複数のモデルタイプをサポートしています。

├── models
│ ├── llm
│ │ ├── chatgpt-4o-latest
│ │ ├── gpt-3.5-turbo
│ │ ├── gpt-4-0125-preview
│ │ ├── gpt-4-turbo
│ │ ├── gpt-4o
│ │ ├── llm
│ │ ├── o1-preview
│ │ └── text-davinci-003
│ ├── moderation
│ │ ├── moderation
│ │ └── text-moderation-stable
│ ├── speech2text
│ │ ├── speech2text
│ │ └── whisper-1
│ ├── text_embedding
│ │ ├── text-embedding-3-large
│ │ └── text_embedding
│ └── tts
│ ├── tts-1-hd
│ ├── tts-1
│ └── tts

### モデルプラグイン作成の準備
モデルプラグインを作成するには、以下の手順に従ってください。

#### 1. モデルプロバイダーの構築
Modelタイプのプラグインを作成する最初のステップは、プラグインプロジェクトを初期化し、モデルプロバイダーファイルを作成することです。その後、具体的な定義済みモデルやカスタムモデルを接続します。

##### 事前準備
- Difyプラグインのスキャフォールディングツール
- Python環境（バージョン3.12以上）

プラグイン開発用のスキャフォールディングツールの準備方法については、開発ツールの初期化を参照してください。

##### 新規プロジェクトの作成

スキャフォールディングツールのコマンドラインから、新しいDifyプラグインプロジェクトを作成します。

<code>
./dify-plugin-darwin-arm64 plugin init
</code>

このバイナリファイルをdifyにリネームし、/usr/local/binにコピーした場合は、次のコマンドで新しいプラグインプロジェクトを作成できます。

<code>
dify plugin init
</code>

##### モデルプラグインテンプレートの選択
スキャフォールディングツール内のすべてのテンプレートには、必要なコードが全て含まれています。LLMタイプのプラグインテンプレートを選択してください。

##### プラグイン権限の設定
このLLMプラグインには、次の権限を設定します。

- Models
- LLM
- Storage

##### モデルタイプ設定の説明
モデルプロバイダーは、以下の2つのモデル設定方法をサポートしています。

- predefined-model 定義済みモデル
    -- 一般的な大規模モデルタイプで、統一されたプロバイダー認証情報を設定するだけで、モデルプロバイダーが提供する定義済みモデルを利用できます。たとえば、OpenAIモデルプロバイダーは、gpt-3.5-turbo-0125やgpt-4o-2024-05-13など、様々な定義済みモデルを提供しています。詳細な開発手順については、定義済みモデルの接続を参照してください。

- customizable-model カスタムモデル
    -- 各モデルの認証情報設定を手動で追加する必要があります。たとえば、XinferenceはLLMとText Embeddingの両方をサポートしていますが、各モデルには一意のmodel_uidがあります。両方を同時に接続する場合は、各モデルにmodel_uidを設定する必要があります。詳細な開発手順については、カスタムモデルの接続を参照してください。

これら2つの設定方法は共存可能です。つまり、プロバイダーがpredefined-modelとcustomizable-modelの両方、またはpredefined-modelのみをサポートしている場合、プロバイダーの統一認証情報を設定することで、定義済みモデルとリモートから取得したモデルを使用できます。さらに、新しいモデルを追加した場合は、それに基づいてカスタムモデルを使用することも可能です。

##### 新しいモデルプロバイダーの追加
新しいモデルプロバイダーを追加するには、主に次の手順が必要です。

1. モデルプロバイダー設定YAMLファイルの作成
プロバイダーディレクトリにYAMLファイルを追加し、プロバイダーの基本情報とパラメータ設定を記述します。ProviderSchemaの要件に従って記述し、システムの仕様との整合性を確保してください。

2. モデルプロバイダーコードの記述
プロバイダークラスのコードを作成します。システムのインターフェース要件に準拠したPythonクラスを実装して、プロバイダーのAPIに接続し、コア機能を実装します。

以下は、各ステップの詳細な操作手順です。

###### 1. モデルプロバイダー設定ファイルの作成
ManifestはYAML形式のファイルで、モデルプロバイダーの基本情報、サポートされているモデルタイプ、設定方法、認証情報ルールを定義します。プラグインプロジェクトのテンプレートには、/providersパスに設定ファイルが自動的に生成されます。

以下は、Anthropicモデルの設定ファイルanthropic.yamlのサンプルコードです。

<sample_code>
provider: anthropic
label:
  en_US: Anthropic
description:
  en_US: Anthropic's powerful models, such as Claude 3.
  zh_Hans: Anthropicの強力なモデル（例：Claude 3）。
icon_small:
  en_US: icon_s_en.svg
icon_large:
  en_US: icon_l_en.svg
background: "#F0F0EB"
help:
  title:
    en_US: Get your API Key from Anthropic
    zh_Hans: AnthropicからAPIキーを取得
  url:
    en_US: https://console.anthropic.com/account/keys
supported_model_types:
  - llm
configurate_methods:
  - predefined-model
provider_credential_schema:
  credential_form_schemas:
    - variable: anthropic_api_key
      label:
        en_US: API Key
      type: secret-input
      required: true
      placeholder:
        zh_Hans: APIキーを入力してください
        en_US: Enter your API Key
    - variable: anthropic_api_url
      label:
        en_US: API URL
      type: text-input
      required: false
      placeholder:
        zh_Hans: API URLを入力してください
        en_US: Enter your API URL
models:
  llm:
    predefined:
      - "models/llm/*.yaml"
    position: "models/llm/_position.yaml"
extra:
  python:
    provider_source: provider/anthropic.py
    model_sources:
      - "models/llm/llm.py"
</sample_code>

接続するプロバイダーがカスタムモデル（たとえば、OpenAIがファインチューニングモデルを提供する場合）を提供する場合は、model_credential_schemaフィールドを追加する必要があります。

以下は、OpenAIファミリーモデルのサンプルコードです。

<sample_code>
model_credential_schema:
  model: # ファインチューニングモデル名
    label:
      en_US: Model Name
      zh_Hans: モデル名
    placeholder:
      en_US: Enter your model name
      zh_Hans: モデル名を入力
  credential_form_schemas:
  - variable: openai_api_key
    label:
      en_US: API Key
    type: secret-input
    required: true
    placeholder:
      zh_Hans: APIキーを入力してください
      en_US: Enter your API Key
  - variable: openai_organization
    label:
        zh_Hans: 組織ID
        en_US: Organization
    type: text-input
    required: false
    placeholder:
      zh_Hans: 組織IDを入力してください
      en_US: Enter your Organization ID
  - variable: openai_api_base
    label:
      zh_Hans: API Base
      en_US: API Base
    type: text-input
    required: false
    placeholder:
      zh_Hans: API Baseを入力してください
      en_US: Enter your API Base
</sample_code>

より詳細なモデルプロバイダーYAMLの仕様については、モデルインターフェースドキュメントを参照してください。

###### 2. モデルプロバイダーコードの記述
/providersフォルダに、同じ名前のPythonファイル（たとえば、anthropic.py）を作成し、__base.provider.Provider基本クラス（たとえば、AnthropicProvider）を継承するclassを実装します。

以下は、Anthropicのサンプルコードです。

<code>
import logging
from dify_plugin.entities.model import ModelType
from dify_plugin.errors.model import CredentialsValidateFailedError
from dify_plugin import ModelProvider

logger = logging.getLogger(__name__)


class AnthropicProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        """
        Validate provider credentials

        if validate failed, raise exception

        :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
        """
        try:
            model_instance = self.get_model_instance(ModelType.LLM)
            model_instance.validate_credentials(model="claude-3-opus-20240229", credentials=credentials)
        except CredentialsValidateFailedError as ex:
            raise ex
        except Exception as ex:
            logger.exception(f"{self.get_provider_schema().provider} credentials validate failed")
            raise ex
</code>

プロバイダーは、__base.model_provider.ModelProvider基底クラスを継承し、validate_provider_credentialsプロバイダー統一認証情報検証メソッドを実装する必要があります。

<code>
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
</code>

もちろん、validate_provider_credentialsの実装を後回しにして、モデル認証情報検証メソッドの実装後に直接再利用することもできます。

##### カスタムモデルプロバイダー
他のタイプのモデルプロバイダーについては、以下の設定方法を参照してください。

Xinferenceのようなカスタムモデルプロバイダーの場合、完全な実装手順を省略できます。XinferenceProviderという名前の空のクラスを作成し、その中に空のvalidate_provider_credentialsメソッドを実装するだけで済みます。

- XinferenceProviderは、カスタムモデルプロバイダーを識別するためのプレースホルダーとして機能します。

- validate_provider_credentialsメソッドは実際には呼び出されませんが、親クラスが抽象クラスであるため、すべてのサブクラスがこのメソッドを実装する必要があります。空の実装を提供することで、抽象メソッドが実装されていないことによるインスタンス化エラーを回避できます。

<code>
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
</code>

モデルプロバイダーを初期化した後、プロバイダーが提供する具体的なLLMモデルを接続する必要があります。詳細については、以下を参照してください。

#### 2. 定義済みモデルの組み込み
モデルプロバイダーの作成が完了していることを確認してください。事前定義済みモデルを組み込むには、以下の手順に従います。

- モデルタイプに応じたモジュール構造の作成
    -- モデルのタイプ（llmやtext_embeddingなど）に応じて、プロバイダーモジュール内に対応するサブモジュールを作成します。各モデルタイプが独立した論理構造を持つようにすることで、保守性と拡張性を高めます。

- モデル呼び出しコードの記述
    -- 対応するモデルタイプのモジュール内に、モデルタイプと同名のPythonファイル（例：llm.py）を作成します。ファイル内に、具体的なモデルロジックを実装するクラスを定義します。このクラスは、システムのモデルインターフェース仕様に準拠している必要があります。

- 事前定義済みモデル設定の追加
    -- プロバイダーが事前定義済みモデルを提供している場合、各モデルに対してモデル名と同名のYAMLファイル（例：claude-3.5.yaml）を作成します。AIModelEntityの仕様に従ってファイルの内容を記述し、モデルのパラメータと機能を定義します。

- プラグインのテスト
    -- 新たに追加されたプロバイダー機能に対して、ユニットテストと統合テストを作成し、すべての機能モジュールが期待どおりに動作することを確認します。

以下は、組み込みの詳細な手順です。

##### 1. モデルタイプに応じたモジュール構造の作成
モデルプロバイダーは、OpenAIが提供するllmやtext_embeddingのように、様々なモデルタイプを提供することがあります。プロバイダーモジュール内に、これらのモデルタイプに対応するサブモジュールを作成し、各モデルタイプが独立した論理構造を持つようにすることで、保守性と拡張性を高めます。

現在サポートされているモデルタイプは以下のとおりです。

- llm: テキスト生成モデル
- text_embedding: テキスト埋め込みモデル
- rerank: Rerankモデル
- speech2text: 音声テキスト変換
- tts: テキスト音声変換
- moderation: 審査

Anthropicを例にとると、そのシリーズモデルにはLLMタイプのモデルのみが含まれているため、/modelsパスに/llmフォルダを新規作成し、異なるモデルのYAMLファイルを追加するだけで済みます。詳細なコード構造については、GitHubコードリポジトリを参照してください。

<path>
├── models
│   └── llm
│       ├── _position.yaml
│       ├── claude-2.1.yaml
│       ├── claude-2.yaml
│       ├── claude-3-5-sonnet-20240620.yaml
│       ├── claude-3-haiku-20240307.yaml
│       ├── claude-3-opus-20240229.yaml
│       ├── claude-3-sonnet-20240229.yaml
│       ├── claude-instant-1.2.yaml
│       ├── claude-instant-1.yaml
│       └── llm.py
</path>

OpenAIのファミリーモデルのように、モデルプロバイダーがllm、text_embedding、moderation、speech2text、ttsなど、さまざまなタイプのモデルを提供している場合は、/modelsパスに各タイプに対応するフォルダを作成する必要があります。構造は以下のようになります。

<path>
├── models
│   ├── common_openai.py
│   ├── llm
│   │   ├── _position.yaml
│   │   ├── chatgpt-4o-latest.yaml
│   │   ├── gpt-3.5-turbo.yaml
│   │   ├── gpt-4-0125-preview.yaml
│   │   ├── gpt-4-turbo.yaml
│   │   ├── gpt-4o.yaml
│   │   ├── llm.py
│   │   ├── o1-preview.yaml
│   │   └── text-davinci-003.yaml
│   ├── moderation
│   │   ├── moderation.py
│   │   └── text-moderation-stable.yaml
│   ├── speech2text
│   │   ├── speech2text.py
│   │   └── whisper-1.yaml
│   ├── text_embedding
│   │   ├── text-embedding-3-large.yaml
│   │   └── text_embedding.py
│   └── tts
│       ├── tts-1-hd.yaml
│   │   ├── tts-1.yaml
│   │   └── tts.py
</path>

すべてのモデル設定を準備してから、モデルコードの実装を開始することをお勧めします。完全なYAMLの記述規則については、モデル設計規則を参照してください。詳細なコードについては、Githubコードリポジトリの例を参照してください。

##### 2. モデル呼び出しコードの記述
次に、/modelsパスにllm.pyというコードファイルを作成する必要があります。Anthropicを例にとると、llm.pyにAnthropic LLMクラスを作成し、AnthropicLargeLanguageModelという名前を付け、__base.large_language_model.LargeLanguageModel基本クラスを継承します。

以下に、一部の機能のサンプルコードを示します。

- LLMの呼び出し
LLMをリクエストする主要なメソッドです。ストリーミングと同期の両方のレスポンスをサポートします。

<code>
def _invoke(self, model: str, credentials: dict,
            prompt_messages: list[PromptMessage], model_parameters: dict,
            tools: Optional[list[PromptMessageTool]] = None, stop: Optional[list[str]] = None,
            stream: bool = True, user: Optional[str] = None) \
        -> Union[LLMResult, Generator]:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param prompt_messages: prompt messages
    :param model_parameters: model parameters
    :param tools: tools for tool calling
    :param stop: stop words
    :param stream: is stream response
    :param user: unique user id
    :return: full response or stream response chunk generator result
    """
</code>

実装時には、同期リターンとストリームリターンを個別に処理するために、2つの関数を使用する必要があることに注意してください。これは、Pythonでyieldキーワードを含む関数はジェネレーター関数として認識され、その戻り値の型がGeneratorに固定されるためです。ロジックを明確にし、様々なリターンの要求に対応するために、同期リターンとストリームリターンは個別に実装する必要があります。

以下はサンプルコードです（サンプルではパラメータが簡略化されています。実際の実装では、完全なパラメータリストに従って記述してください）。

<code>
def _invoke(self, stream: bool, **kwargs) -> Union[LLMResult, Generator]:
    """戻り値の型に応じて、対応する処理関数を呼び出します。"""
    if stream:
        return self._handle_stream_response(**kwargs)
    return self._handle_sync_response(**kwargs)

def _handle_stream_response(self, **kwargs) -> Generator:
    """ストリームリターンのロジックを処理します。"""
    for chunk in response:  # responseがストリームデータのイテレーターであると仮定します
        yield chunk

def _handle_sync_response(self, **kwargs) -> LLMResult:
    """同期リターンのロジックを処理します。"""
    return LLMResult(**response)  # responseが完全な応答の辞書であると仮定します
</code>

- 入力トークン数の事前計算
モデルがトークン数の事前計算インターフェースを提供していない場合は、この機能が適用されないか、実装されていないことを示すために、直接0を返すことができます。例：

<code>
def get_num_tokens(self, model: str, credentials: dict, prompt_messages: list[PromptMessage],
                   tools: Optional[list[PromptMessageTool]] = None) -> int:
    """
    Get number of tokens for given prompt messages

    :param model: model name
    :param credentials: model credentials
    :param prompt_messages: prompt messages
    :param tools: tools for tool calling
    :return:
    """
</code>

- 呼び出し例外エラーマッピングテーブル

モデル呼び出しが例外の場合、Difyがさまざまなエラーに対して適切な処理を実行できるように、Runtimeによって指定されたInvokeErrorタイプにマッピングする必要があります。

Runtime Errors:
- InvokeConnectionError: 呼び出し接続エラー
- InvokeServerUnavailableError: 呼び出しサービスが利用不可
- InvokeRateLimitError: 呼び出しが制限に達しました
- InvokeAuthorizationError: 呼び出し認証に失敗しました
- InvokeBadRequestError: 呼び出しパラメータにエラーがあります

<code>
@property
def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
    """
    Map model invoke error to unified error
    The key is the error type thrown to the caller
    The value is the error type thrown by the model,
    which needs to be converted into a unified error type for the caller.

    :return: Invoke error mapping
    """
</code>

完全なコードの詳細については、Githubコードリポジトリを参照してください。

##### 3. 事前定義済みモデル設定の追加
プロバイダーが事前定義済みモデルを提供している場合、各モデルに対してモデル名と同名のYAMLファイル（例：claude-3.5.yaml）を作成します。AIModelEntityの仕様に従ってファイルの内容を記述し、モデルのパラメータと機能を定義します。

claude-3-5-sonnet-20240620モデルのサンプルコード：

<code>
model: claude-3-5-sonnet-20240620
label:
  en_US: claude-3-5-sonnet-20240620
model_type: llm
features:
  - agent-thought
  - vision
  - tool-call
  - stream-tool-call
  - document
model_properties:
  mode: chat
  context_size: 200000
parameter_rules:
  - name: temperature
    use_template: temperature
  - name: top_p
    use_template: top_p
  - name: top_k
    label:
      zh_Hans: 取样数量
      en_US: Top k
    type: int
    help:
      zh_Hans: 仅从每个后续标记的前 K 个选项中采样。
      en_US: Only sample from the top K options for each subsequent token.
    required: false
  - name: max_tokens
    use_template: max_tokens
    required: true
    default: 8192
    min: 1
    max: 8192
  - name: response_format
    use_template: response_format
pricing:
  input: '3.00'
  output: '15.00'
  unit: '0.000001'
  currency: USD
</code>

##### 4. プラグインのデバッグ
次に、プラグインが正常に動作するかどうかをテストする必要があります。Difyはリモートデバッグ方法を提供しており、「プラグイン管理」ページでデバッグキーとリモートサーバーアドレスを取得できます。

プラグインプロジェクトに戻り、.env.exampleファイルをコピーして.envにリネームし、取得したリモートサーバーアドレスとデバッグKeyなどの情報を入力します。

<.env_file>
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
</.env_file>

python -m mainコマンドを実行してプラグインを起動します。プラグインページで、そのプラグインがWorkspaceにインストールされていることを確認できます。他のチームメンバーもこのプラグインにアクセスできます。

「設定」→「モデルプロバイダー」でAPI Keyを入力して、モデルプロバイダーを初期化できます。


##### プラグインの公開
作成したプラグインをDify Pluginsコードリポジトリにアップロードして公開できます。アップロードする前に、プラグインがプラグイン公開仕様に準拠していることを確認してください。審査に合格すると、コードがメインブランチにマージされ、Dify Marketplaceに自動的に公開されます。


#### 3. カスタムモデルの組み込み
##### カスタムモデルの組み込み
カスタムモデルとは、ユーザー自身でデプロイまたは設定する必要があるLLMのことです。この記事では、Xinferenceモデルを例に、モデルプラグイン内でカスタムモデルを組み込む方法を解説します。

カスタムモデルには、デフォルトでモデルタイプとモデル名の2つのパラメータが含まれており、サプライヤのyamlファイルで定義する必要はありません。

サプライヤ設定ファイルでvalidate_provider_credentialを実装する必要はありません。Runtimeは、ユーザーが選択したモデルタイプまたはモデル名に基づいて、対応するモデルレイヤのvalidate_credentialsメソッドを自動的に呼び出して検証します。

##### カスタムモデルプラグインの組み込み
カスタムモデルを組み込むには、以下の手順に従います。

- 1.モデルサプライヤファイルの作成
組み込むカスタムモデルのモデルタイプを明確にします。

- 2.モデルタイプに応じたコードファイルの作成
モデルのタイプ（llmやtext_embeddingなど）に応じて、コードファイルを作成します。各モデルタイプが独立した論理構造を持つようにすることで、保守と拡張が容易になります。

- 3.モデルモジュールに基づいたモデル呼び出しコードの記述
対応するモデルタイプモジュールに、モデルタイプと同名のPythonファイル（例：llm.py）を作成します。ファイル内で、具体的なモデルロジックを実装するクラスを定義します。このクラスは、システムのモデルインターフェース仕様に準拠している必要があります。

- 4.プラグインのデバッグ
新たに追加されたサプライヤ機能について、ユニットテストと統合テストを作成し、すべての機能モジュールが期待どおりに動作することを確認します。

###### 1. モデルサプライヤファイルの作成
プラグインプロジェクトの/providerパスに、xinference.yamlファイルを作成します。

Xinferenceは、LLM、Text Embedding、Rerankのモデルタイプをサポートしているため、xinference.yamlファイルにこれらのモデルタイプを含める必要があります。

サンプルコード：
<sample_code>
provider: xinference # サプライヤIDを決定
label: # サプライヤの表示名。en_US（英語）とzh_Hans（中国語）の2つの言語を設定できます。zh_Hansを設定しない場合、デフォルトでen_USが使用されます。
  en_US: Xorbits Inference
icon_small: # 小さいアイコン。他のサプライヤのアイコンを参考に、対応するサプライヤ実装ディレクトリの_assetsディレクトリに保存してください。言語設定はlabelと同様です。
  en_US: icon_s_en.svg
icon_large: # 大きいアイコン
  en_US: icon_l_en.svg
help: # ヘルプ
  title:
    en_US: How to deploy Xinference
    zh_Hans: 如何部署 Xinference (Xinferenceのデプロイ方法)
  url:
    en_US: https://github.com/xorbitsai/inference
supported_model_types: # サポートされているモデルタイプ。XinferenceはLLM/Text Embedding/Rerankをサポートしています。
- llm
- text-embedding
- rerank
configurate_methods: # Xinferenceはローカルにデプロイするサプライヤであり、事前定義されたモデルはありません。使用するモデルはXinferenceのドキュメントに従ってデプロイする必要があるため、ここではカスタムモデルを使用します。
- customizable-model
provider_credential_schema:
  credential_form_schemas:
</sample_code>

次に、provider_credential_schemaフィールドを定義します。Xinferenceは、text-generation、embeddings、rerankingモデルをサポートしています。サンプルコードを以下に示します。

<sample_code>
provider_credential_schema:
  credential_form_schemas:
  - variable: model_type
    type: select
    label:
      en_US: Model type
      zh_Hans: 模型类型 (モデルタイプ)
    required: true
    options:
    - value: text-generation
      label:
        en_US: Language Model
        zh_Hans: 语言模型 (言語モデル)
    - value: embeddings
      label:
        en_US: Text Embedding
    - value: reranking
      label:
        en_US: Rerank
</sample_code>

Xinferenceの各モデルでは、model_nameという名前を定義する必要があります。

<sample_code>
  - variable: model_name
    type: text-input
    label:
      en_US: Model name
      zh_Hans: 模型名称 (モデル名)
    required: true
    placeholder:
      zh_Hans: モデル名を入力してください
      en_US: Input model name
</sample_code>

Xinferenceモデルでは、ユーザーがモデルのローカルデプロイアドレスを入力する必要があります。プラグイン内では、Xinferenceモデルのローカルデプロイアドレス（server_url）とモデルUIDを入力できる場所を提供する必要があります。サンプルコードを以下に示します。

<sample_code>
  - variable: server_url
    label:
      zh_Hans: サーバーURL
      en_US: Server url
    type: text-input
    required: true
    placeholder:
      zh_Hans: Xinferenceのサーバーアドレスをここに入力してください（例：https://example.com/xxx）
      en_US: Enter the url of your Xinference, for example https://example.com/xxx
  - variable: model_uid
    label:
      zh_Hans: モデルUID
      en_US: Model uid
    type: text-input
    required: true
    placeholder:
      zh_Hans: モデルUIDを入力してください
      en_US: Enter the model uid
すべてのパラメータを入力すると、カスタムモデルサプライヤのyaml設定ファイルの作成が完了します。次に、設定ファイルで定義されたモデルに具体的な機能コードファイルを追加する必要があります。
</sample_code>

###### 2. モデルコードの記述
Xinferenceモデルサプライヤのモデルタイプには、llm、rerank、speech2text、ttsタイプが含まれています。そのため、/modelsパスに各モデルタイプの独立したグループを作成し、対応する機能コードファイルを作成する必要があります。

以下では、llmタイプを例に、llm.pyコードファイルの作成方法を説明します。コードを作成する際には、Xinference LLMクラスを作成する必要があります。名前はXinferenceAILargeLanguageModelとし、__base.large_language_model.LargeLanguageModel基底クラスを継承し、以下のメソッドを実装します。

- LLMの呼び出し
LLM呼び出しの中核となるメソッドです。ストリーミングと同期の両方の戻り値をサポートします。

<code>
def _invoke(self, model: str, credentials: dict,
            prompt_messages: list[PromptMessage], model_parameters: dict,
            tools: Optional[list[PromptMessageTool]] = None, stop: Optional[list[str]] = None,
            stream: bool = True, user: Optional[str] = None) \
        -> Union[LLMResult, Generator]:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param prompt_messages: prompt messages
    :param model_parameters: model parameters
    :param tools: tools for tool calling
    :param stop: stop words
    :param stream: is stream response
    :param user: unique user id
    :return: full response or stream response chunk generator result
    """
</code>

コードを実装する際には、同期戻り値とストリーミング戻り値で異なる関数を使用する必要があります。

Pythonでは、関数にyieldキーワードが含まれている場合、その関数はジェネレータ関数として認識され、戻り値の型はGeneratorに固定されます。したがって、同期戻り値とストリーミング戻り値をそれぞれ実装する必要があります。例えば、以下のサンプルコードを参照してください。

この例では、パラメータが簡略化されています。実際のコードを記述する際には、上記のパラメータリストを参照してください。

<code>
def _invoke(self, stream: bool, **kwargs) \
        -> Union[LLMResult, Generator]:
    if stream:
          return self._handle_stream_response(**kwargs)
    return self._handle_sync_response(**kwargs)

def _handle_stream_response(self, **kwargs) -> Generator:
    for chunk in response:
          yield chunk
def _handle_sync_response(self, **kwargs) -> LLMResult:
    return LLMResult(**response)
</code>

- 入力トークンの事前計算
モデルがトークンの事前計算インターフェースを提供していない場合は、0を返すことができます。

<code>
def get_num_tokens(self, model: str, credentials: dict, prompt_messages: list[PromptMessage],
                 tools: Optional[list[PromptMessageTool]] = None) -> int:
  """
  Get number of tokens for given prompt messages

  :param model: model name
  :param credentials: model credentials
  :param prompt_messages: prompt messages
  :param tools: tools for tool calling
  :return:
  """
</code>

直接0を返したくない場合は、self._get_num_tokens_by_gpt2(text: str)メソッドを使用してトークンを計算できます。このメソッドはAIModel基底クラスにあり、GPT-2のTokenizerを使用して計算を行います。ただし、あくまで代替手段であり、計算結果には誤差が生じる可能性があることに注意してください。

- モデルの認証情報の検証
サプライヤの認証情報の検証と同様に、ここでは個々のモデルを検証します。

<code>
def validate_credentials(self, model: str, credentials: dict) -> None:
    """
    Validate model credentials

    :param model: model name
    :param credentials: model credentials
    :return:
    """
</code>

- モデルパラメータのスキーマ
事前定義されたモデルタイプとは異なり、YAMLファイルにモデルがサポートするパラメータが事前に定義されていないため、モデルパラメータのスキーマを動的に生成する必要があります。

例えば、Xinferenceはmax_tokens、temperature、top_pの3つのモデルパラメータをサポートしています。ただし、サプライヤによっては、モデルごとに異なるパラメータをサポートする場合があります（例：OpenLLM）。

例として、サプライヤOpenLLMのモデルAはtop_kパラメータをサポートしていますが、モデルBはサポートしていません。この場合、各モデルに対応するパラメータスキーマを動的に生成する必要があります。以下にサンプルコードを示します。

<code>
def get_customizable_model_schema(self, model: str, credentials: dict) -> AIModelEntity | None:
    """
        used to define customizable model schema
    """
    rules = [
        ParameterRule(
            name='temperature', type=ParameterType.FLOAT,
            use_template='temperature',
            label=I18nObject(
                zh_Hans='温度', en_US='Temperature'
            )
        ),
        ParameterRule(
            name='top_p', type=ParameterType.FLOAT,
            use_template='top_p',
            label=I18nObject(
                zh_Hans='Top P', en_US='Top P'
            )
        ),
        ParameterRule(
            name='max_tokens', type=ParameterType.INT,
            use_template='max_tokens',
            min=1,
            default=512,
            label=I18nObject(
                zh_Hans='最大生成长度', en_US='Max Tokens'
            )
        )
    ]

    # if model is A, add top_k to rules
    if model == 'A':
        rules.append(
            ParameterRule(
                name='top_k', type=ParameterType.INT,
                use_template='top_k',
                min=1,
                default=50,
                label=I18nObject(
                    zh_Hans='Top K', en_US='Top K'
                )
            )
        )

    """
        some NOT IMPORTANT code here
    """

    entity = AIModelEntity(
        model=model,
        label=I18nObject(
            en_US=model
        ),
        fetch_from=FetchFrom.CUSTOMIZABLE_MODEL,
        model_type=model_type,
        model_properties={ 
            ModelPropertyKey.MODE:  ModelType.LLM,
        },
        parameter_rules=rules
    )

    return entity
</code>

- 呼び出し例外エラーのマッピング

モデルの呼び出し時に例外が発生した場合、Runtimeで指定されたInvokeErrorタイプにマッピングする必要があります。これは、Difyが異なるエラーに対して異なる後続処理を実行できるようにするためです。

Runtime Errors:
- `InvokeConnectionError`  呼び出し接続エラー
- `InvokeServerUnavailableError`  呼び出しサービスが利用不可
- `InvokeRateLimitError` 呼び出しが制限に達した
- `InvokeAuthorizationError` 呼び出し認証失敗
- `InvokeBadRequestError` 呼び出しパラメータエラー

<code>
@property
def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
    """
    Map model invoke error to unified error
    The key is the error type thrown to the caller
    The value is the error type thrown by the model,
    which needs to be converted into a unified error type for the caller.

    :return: Invoke error mapping
    """
</code>

さらに詳しいインターフェースメソッドについては、インターフェースドキュメント：Modelを参照してください。

この記事で取り上げた完全なコードファイルについては、GitHubコードリポジトリをご覧ください。

###### 3. プラグインのデバッグ
プラグインの開発が完了したら、次にプラグインが正常に動作するかどうかをテストする必要があります。詳細については、以下を参照してください。

###### 4. プラグインの公開
プラグインをDify マーケットプレイスに公開する場合は、以下を参照してください。

### エージェント戦略プラグイン
エージェント戦略プラグインは、LLMが推論や意思決定ロジックを実行するのを支援します。具体的には、ツール選択、呼び出し、結果処理といった一連の動作をより自動化された方法で実行し、問題を解決します。

この記事では、ツール呼び出し（Function Calling）機能を備え、現在の正確な時刻を自動的に取得するプラグインの作成方法を説明します。

#### 事前準備
- Difyプラグインの足場ツール
- Python環境（バージョン3.12以上）

プラグイン開発の足場ツールを準備する方法については、開発ツールの初期化を参照してください。

- ヒント：ターミナルで dify version コマンドを実行し、バージョン番号が表示されることを確認することで、足場ツールが正常にインストールされたことを確認できます。

#### 1. プラグインテンプレートの初期化
以下のコマンドを実行して、Agentプラグイン開発テンプレートを初期化します。

<code>
dify plugin init
</code>

表示される指示に従い、必要な情報を入力します。以下のコードのコメントを参考に設定してください。

<example>
➜  Dify Plugins Developing dify plugin init
Edit profile of the plugin
Plugin name (press Enter to next step): # プラグインの名前を入力
Author (press Enter to next step): Author name # プラグインの作者を入力
Description (press Enter to next step): Description # プラグインの説明を入力
---
Select the language you want to use for plugin development, and press Enter to con
BTW, you need Python 3.12+ to develop the Plugin if you choose Python.
-> python # Python環境を選択
  go (not supported yet)
---
Based on the ability you want to extend, we have divided the Plugin into four type

- Tool: It's a tool provider, but not only limited to tools, you can implement an 
- Model: Just a model provider, extending others is not allowed.
- Extension: Other times, you may only need a simple http service to extend the fu
- Agent Strategy: Implement your own logics here, just by focusing on Agent itself

What's more, we have provided the template for you, you can choose one of them b
  tool
-> agent-strategy # エージェント戦略テンプレートを選択
  llm
  text-embedding
---
Configure the permissions of the plugin, use up and down to navigate, tab to sel
Backwards Invocation:
Tools:
    Enabled: [✔]  You can invoke tools inside Dify if it's enabled # デフォルトで有効
Models:
    Enabled: [✔]  You can invoke models inside Dify if it's enabled # デフォルトで有効
    LLM: [✔]  You can invoke LLM models inside Dify if it's enabled # デフォルトで有効
    Text Embedding: [✘]  You can invoke text embedding models inside Dify if it'
    Rerank: [✘]  You can invoke rerank models inside Dify if it's enabled
...
</example>

プラグインテンプレートを初期化すると、プラグインの開発に必要なすべてのリソースを含むコードフォルダが生成されます。エージェント戦略プラグインのコード構造を理解することで、開発プロセスがスムーズになります。

<path>
├── GUIDE.md               # ユーザーガイドとドキュメント
├── PRIVACY.md            # プライバシーポリシーとデータ処理ガイドライン
├── README.md             # プロジェクト概要と設定手順
├── _assets/             # 静的アセットディレクトリ
│   └── icon.svg         # エージェント戦略プロバイダーのアイコン/ロゴ
├── main.py              # メインアプリケーションのエントリーポイント
├── manifest.yaml        # 基本的なプラグイン構成
├── provider/           # プロバイダー構成ディレクトリ
│   └── basic_agent.yaml # Agentプロバイダーの設定
├── requirements.txt    # Python依存関係リスト
└── strategies/         # 戦略実装ディレクトリ
    ├── basic_agent.py  # 基本的なエージェント戦略の実装
    └── basic_agent.yaml # 基本的なエージェント戦略の構成
</path>

プラグインの機能コードは、strategies/ ディレクトリにまとめられています。

#### 2. プラグイン機能の開発
エージェントプラグインの開発は、主に以下の2つのファイルを中心に行います。

- プラグイン定義ファイル：strategies/basic_agent.yaml
- プラグイン機能コード：strategies/basic_agent.py

##### 2.1 パラメータの定義
Agentプラグインを作成するには、まず strategies/basic_agent.yaml ファイルでプラグインに必要なパラメータを定義します。これらのパラメータは、LLMモデルの呼び出しやツールの使用など、プラグインの核となる機能を決定します。

次の4つの基本パラメータを優先的に設定することをお勧めします。

- model：呼び出すLLM（GPT-4、GPT-4o-miniなど）を指定します。
- tools：プラグインが使用できるツールリストを定義し、プラグインの機能を拡張します。
- query：モデルとの対話に使用するプロンプトまたは入力内容を設定します。
- maximum_iterations：プラグインの最大反復回数を制限し、過剰な計算を避けます。

<code>
identity:
  name: basic_agent # agent_strategyの名前
  author: novice # agent_strategyの作者
  label:
    en_US: BasicAgent # agent_strategyの英語ラベル
description:
  en_US: BasicAgent # agent_strategyの英語説明
parameters:
  - name: model # modelパラメータの名前
    type: model-selector # model-type
    scope: tool-call&llm # パラメータのスコープ
    required: true
    label:
      en_US: Model
      zh_Hans: 模型
      pt_BR: Model
  - name: tools # toolsパラメータの名前
    type: array[tools] # toolパラメータの型
    required: true
    label:
      en_US: Tools list
      zh_Hans: 工具列表
      pt_BR: Tools list
  - name: query # queryパラメータの名前
    type: string # queryパラメータの型
    required: true
    label:
      en_US: Query
      zh_Hans: 查询
      pt_BR: Query
  - name: maximum_iterations
    type: number
    required: false
    default: 5
    label:
      en_US: Maxium Iterations
      zh_Hans: 最大迭代次数
      pt_BR: Maxium Iterations
    max: 50 # maxとminの値を設定すると、パラメータ表示がスライダーになります
    min: 1
extra:
  python:
    source: strategies/basic_agent.py
</code>

パラメータ設定が完了すると、プラグインは対応する設定ページを自動的に生成し、直感的かつ使いやすく調整や利用ができます。

##### 2.2 パラメータの取得と実行
ユーザーがプラグインの設定ページで基本情報を入力すると、プラグインは入力されたパラメータを処理する必要があります。そのため、まず strategies/basic_agent.py ファイル内で、後で使用するためのAgentパラメータクラスを定義します。

入力パラメータの検証：

<code>
from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity
from pydantic import BaseModel

class BasicParams(BaseModel):
    maximum_iterations: int
    model: AgentModelConfig
    tools: list[ToolEntity]
    query: str
</code>

パラメータを取得した後、具体的な処理ロジックを実行します。

<code>
class BasicAgentAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        params = BasicParams(**parameters)
</code>

#### 3. モデルの呼び出し
エージェント戦略プラグインでは、モデルの呼び出しが中心的な処理ロジックの1つです。SDKが提供する session.model.llm.invoke() メソッドを使用すると、LLMモデルを効率的に呼び出して、テキスト生成や対話処理などの機能を実現できます。

モデルにツール呼び出し機能を持たせたい場合は、まず、モデルがツール呼び出し形式に沿ったパラメータを出力できることを確認する必要があります。つまり、モデルはユーザーの指示に従って、ツールインターフェースの要件を満たすパラメータを生成する必要があります。

以下のパラメータを構築します。

- model：モデル情報
- prompt_messages：プロンプト
- tools：ツール情報（Function Calling関連）
- stop：停止記号
- stream：ストリーミング出力をサポートするかどうか

メソッド定義のサンプルコード：
<code>
def invoke(
        self,
        model_config: LLMModelConfig,
        prompt_messages: list[PromptMessage],
        tools: list[PromptMessageTool] | None = None,
        stop: list[str] | None = None,
        stream: bool = True,
    ) -> Generator[LLMResultChunk, None, None] | LLMResult:...
</code>

完全な実装については、モデル呼び出しのサンプルコードを参照してください。

このコードでは、ユーザーが指示を入力すると、エージェント戦略プラグインが自動的にLLMを呼び出し、その結果に基づいてツールの呼び出しに必要なパラメータを構築し、渡します。これにより、モデルは連携されたツールを柔軟に活用し、複雑なタスクを効率的に完了できます。

#### 4. ツールの呼び出し
ツールパラメータを設定した後、エージェント戦略プラグインに実際にツールを呼び出す機能を追加する必要があります。これは、SDKの session.tool.invoke() 関数を使用して行えます。

以下のパラメータを構築します。
- provider：ツール提供者
- tool_name：ツール名
- parameters：入力パラメータ

メソッド定義のサンプルコード：
<code>
 def invoke(
        self,
        provider_type: ToolProviderType,
        provider: str,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]:...
</code>

LLMで直接パラメータを生成してツールを呼び出したい場合は、以下のツール呼び出しのサンプルコードを参照してください。

<code>
tool_instances = (
    {tool.identity.name: tool for tool in params.tools} if params.tools else {}
)
for tool_call_id, tool_call_name, tool_call_args in tool_calls:
    tool_instance = tool_instances[tool_call_name]
    self.session.tool.invoke(
        provider_type=ToolProviderType.BUILT_IN,
        provider=tool_instance.identity.provider,
        tool_name=tool_instance.identity.name,
        parameters={**tool_instance.runtime_parameters, **tool_call_args},
    )
</code>

完全な機能コードについては、ツール呼び出しのサンプルコードを参照してください。

この機能コードを実装すると、エージェント戦略プラグインは自動的にFunction Callingを実行できるようになります。例えば、現在の時刻を自動的に取得するなどが可能です。


#### 5. ログの作成
エージェント戦略プラグインでは、複雑なタスクを完了するために、通常、複数回の操作が必要です。各操作の実行結果を記録することは、開発者にとって非常に重要です。Agentの実行プロセスを追跡し、各ステップの意思決定の根拠を分析することで、戦略の効果をより適切に評価し、最適化できます。

この機能を実装するために、SDKの create_log_message と finish_log_message メソッドを利用してログを記録できます。この方法では、モデル呼び出しの前後に操作状態をリアルタイムで記録できるだけでなく、開発者が問題を迅速に特定するのに役立ちます。

シナリオ例：

- モデルを呼び出す前に、「モデルの呼び出しを開始」というログを記録することで、開発者はタスクの実行状況を明確に把握できます。
- モデル呼び出しが成功した後、「呼び出し成功」というログを記録することで、モデルの応答の完全性を追跡できます。

<code>
model_log = self.create_log_message(
            label=f"{params.model.model} Thought",
            data={},
            metadata={"start_at": model_started_at, "provider": params.model.provider},
            status=ToolInvokeMessage.LogMessage.LogStatus.START,
        )
yield model_log
self.session.model.llm.invoke(...)
yield self.finish_log_message(
    log=model_log,
    data={
        "output": response,
        "tool_name": tool_call_names,
        "tool_input": tool_call_inputs,
    },
    metadata={
        "started_at": model_started_at,
        "finished_at": time.perf_counter(),
        "elapsed_time": time.perf_counter() - model_started_at,
        "provider": params.model.provider,
    },
)
</code>

設定が完了すると、ワークフローログに実行結果が出力されます。

Agentの実行中には、複数ラウンドのログが生成される場合があります。ログに階層構造を持たせることで、開発者がログを確認しやすくなります。ログを記録する際に parent パラメータを渡すことで、異なるラウンドのログ間に親子関係が形成され、ログの表示がより明確になり、追跡が容易になります。

使用方法：
<code>
function_call_round_log = self.create_log_message(
    label="Function Call Round1 ",
    data={},
    metadata={},
)
yield function_call_round_log

model_log = self.create_log_message(
    label=f"{params.model.model} Thought",
    data={},
    metadata={"start_at": model_started_at, "provider": params.model.provider},
    status=ToolInvokeMessage.LogMessage.LogStatus.START,
    # 親ログを追加
    parent=function_call_round_log,
)
yield model_log
</code>

##### プラグイン機能のサンプルコード：

<モデルの呼び出し>
以下のコードは、エージェント戦略プラグインにモデルを呼び出す機能を追加する方法を示しています。
<code>
import json
from collections.abc import Generator
from typing import Any, cast

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig, LLMResult, LLMResultChunk
from dify_plugin.entities.model.message import (
    PromptMessageTool,
    UserPromptMessage,
)
from dify_plugin.entities.tool import ToolInvokeMessage, ToolParameter, ToolProviderType
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity
from pydantic import BaseModel

class BasicParams(BaseModel):
    maximum_iterations: int
    model: AgentModelConfig
    tools: list[ToolEntity]
    query: str

class BasicAgentAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        params = BasicParams(**parameters)
        chunks: Generator[LLMResultChunk, None, None] | LLMResult = (
            self.session.model.llm.invoke(
                model_config=LLMModelConfig(**params.model.model_dump(mode="json")),
                prompt_messages=[UserPromptMessage(content=params.query)],
                tools=[
                    self._convert_tool_to_prompt_message_tool(tool)
                    for tool in params.tools
                ],
                stop=params.model.completion_params.get("stop", [])
                if params.model.completion_params
                else [],
                stream=True,
            )
        )
        response = ""
        tool_calls = []
        tool_instances = (
            {tool.identity.name: tool for tool in params.tools} if params.tools else {}
        )

        for chunk in chunks:
            # ツール呼び出しがあるか確認
            if self.check_tool_calls(chunk):
                tool_calls = self.extract_tool_calls(chunk)
                tool_call_names = ";".join([tool_call[1] for tool_call in tool_calls])
                try:
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls},
                        ensure_ascii=False,
                    )
                except json.JSONDecodeError:
                    # エンコードエラーを避けるため、asciiを保証
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls}
                    )
                print(tool_call_names, tool_call_inputs)
            if chunk.delta.message and chunk.delta.message.content:
                if isinstance(chunk.delta.message.content, list):
                    for content in chunk.delta.message.content:
                        response += content.data
                        print(content.data, end="", flush=True)
                else:
                    response += str(chunk.delta.message.content)
                    print(str(chunk.delta.message.content), end="", flush=True)

            if chunk.delta.usage:
                # モデルを使用する
                usage = chunk.delta.usage

        yield self.create_text_message(
            text=f"{response or json.dumps(tool_calls, ensure_ascii=False)}\n"
        )
        result = ""
        for tool_call_id, tool_call_name, tool_call_args in tool_calls:
            tool_instance = tool_instances[tool_call_name]
            tool_invoke_responses = self.session.tool.invoke(
                provider_type=ToolProviderType.BUILT_IN,
                provider=tool_instance.identity.provider,
                tool_name=tool_instance.identity.name,
                parameters={**tool_instance.runtime_parameters, **tool_call_args},
            )
            if not tool_instance:
                tool_invoke_responses = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": f"there is not a tool named {tool_call_name}",
                }
            else:
                # ツールを呼び出す
                tool_invoke_responses = self.session.tool.invoke(
                    provider_type=ToolProviderType.BUILT_IN,
                    provider=tool_instance.identity.provider,
                    tool_name=tool_instance.identity.name,
                    parameters={**tool_instance.runtime_parameters, **tool_call_args},
                )
                result = ""
                for tool_invoke_response in tool_invoke_responses:
                    if tool_invoke_response.type == ToolInvokeMessage.MessageType.TEXT:
                        result += cast(
                            ToolInvokeMessage.TextMessage, tool_invoke_response.message
                        ).text
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.LINK
                    ):
                        result += (
                            f"result link: {cast(ToolInvokeMessage.TextMessage, tool_invoke_response.message).text}."
                            + " please tell user to check it."
                        )
                    elif tool_invoke_response.type in {
                        ToolInvokeMessage.MessageType.IMAGE_LINK,
                        ToolInvokeMessage.MessageType.IMAGE,
                    }:
                        result += (
                            "image has been created and sent to user already, "
                            + "you do not need to create it, just tell the user to check it now."
                        )
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.JSON
                    ):
                        text = json.dumps(
                            cast(
                                ToolInvokeMessage.JsonMessage,
                                tool_invoke_response.message,
                            ).json_object,
                            ensure_ascii=False,
                        )
                        result += f"tool response: {text}."
                    else:
                        result += f"tool response: {tool_invoke_response.message!r}."

                tool_response = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": result,
                }
        yield self.create_text_message(result)

    def _convert_tool_to_prompt_message_tool(
        self, tool: ToolEntity
    ) -> PromptMessageTool:
        """
        convert tool to prompt message tool
        """
        message_tool = PromptMessageTool(
            name=tool.identity.name,
            description=tool.description.llm if tool.description else "",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )

        parameters = tool.parameters
        for parameter in parameters:
            if parameter.form != ToolParameter.ToolParameterForm.LLM:
                continue

            parameter_type = parameter.type
            if parameter.type in {
                ToolParameter.ToolParameterType.FILE,
                ToolParameter.ToolParameterType.FILES,
            }:
                continue
            enum = []
            if parameter.type == ToolParameter.ToolParameterType.SELECT:
                enum = (
                    [option.value for option in parameter.options]
                    if parameter.options
                    else []
                )

            message_tool.parameters["properties"][parameter.name] = {
                "type": parameter_type,
                "description": parameter.llm_description or "",
            }

            if len(enum) > 0:
                message_tool.parameters["properties"][parameter.name]["enum"] = enum

            if parameter.required:
                message_tool.parameters["required"].append(parameter.name)

        return message_tool

    def check_tool_calls(self, llm_result_chunk: LLMResultChunk) -> bool:
        """
        Check if there is any tool call in llm result chunk
        """
        return bool(llm_result_chunk.delta.message.tool_calls)

    def extract_tool_calls(
        self, llm_result_chunk: LLMResultChunk
    ) -> list[tuple[str, str, dict[str, Any]]]:
        """
        Extract tool calls from llm result chunk

        Returns:
            List[Tuple[str, str, Dict[str, Any]]]: [(tool_call_id, tool_call_name, tool_call_args)]
        """
        tool_calls = []
        for prompt_message in llm_result_chunk.delta.message.tool_calls:
            args = {}
            if prompt_message.function.arguments != "":
                args = json.loads(prompt_message.function.arguments)

            tool_calls.append(
                (
                    prompt_message.id,
                    prompt_message.function.name,
                    args,
                )
            )

        return tool_calls
</code>
</モデルの呼び出し>

<ツールの呼び出し>
次のコードは、エージェント戦略プラグインのモデル呼び出しを実装し、正規化されたリクエストをツールに送信する方法を示しています。
<code>
import json
from collections.abc import Generator
from typing import Any, cast

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig, LLMResult, LLMResultChunk
from dify_plugin.entities.model.message import (
    PromptMessageTool,
    UserPromptMessage,
)
from dify_plugin.entities.tool import ToolInvokeMessage, ToolParameter, ToolProviderType
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity
from pydantic import BaseModel

class BasicParams(BaseModel):
    maximum_iterations: int
    model: AgentModelConfig
    tools: list[ToolEntity]
    query: str

class BasicAgentAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        params = BasicParams(**parameters)
        chunks: Generator[LLMResultChunk, None, None] | LLMResult = (
            self.session.model.llm.invoke(
                model_config=LLMModelConfig(**params.model.model_dump(mode="json")),
                prompt_messages=[UserPromptMessage(content=params.query)],
                tools=[
                    self._convert_tool_to_prompt_message_tool(tool)
                    for tool in params.tools
                ],
                stop=params.model.completion_params.get("stop", [])
                if params.model.completion_params
                else [],
                stream=True,
            )
        )
        response = ""
        tool_calls = []
        tool_instances = (
            {tool.identity.name: tool for tool in params.tools} if params.tools else {}
        )

        for chunk in chunks:
            # ツール呼び出しがあるか確認
            if self.check_tool_calls(chunk):
                tool_calls = self.extract_tool_calls(chunk)
                tool_call_names = ";".join([tool_call[1] for tool_call in tool_calls])
                try:
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls},
                        ensure_ascii=False,
                    )
                except json.JSONDecodeError:
                    # エンコードエラーを避けるため、asciiを保証
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls}
                    )
                print(tool_call_names, tool_call_inputs)
            if chunk.delta.message and chunk.delta.message.content:
                if isinstance(chunk.delta.message.content, list):
                    for content in chunk.delta.message.content:
                        response += content.data
                        print(content.data, end="", flush=True)
                else:
                    response += str(chunk.delta.message.content)
                    print(str(chunk.delta.message.content), end="", flush=True)

            if chunk.delta.usage:
                # モデルを使用する
                usage = chunk.delta.usage

        yield self.create_text_message(
            text=f"{response or json.dumps(tool_calls, ensure_ascii=False)}\n"
        )
        result = ""
        for tool_call_id, tool_call_name, tool_call_args in tool_calls:
            tool_instance = tool_instances[tool_call_name]
            tool_invoke_responses = self.session.tool.invoke(
                provider_type=ToolProviderType.BUILT_IN,
                provider=tool_instance.identity.provider,
                tool_name=tool_instance.identity.name,
                parameters={**tool_instance.runtime_parameters, **tool_call_args},
            )
            if not tool_instance:
                tool_invoke_responses = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": f"there is not a tool named {tool_call_name}",
                }
            else:
                # ツールを呼び出す
                tool_invoke_responses = self.session.tool.invoke(
                    provider_type=ToolProviderType.BUILT_IN,
                    provider=tool_instance.identity.provider,
                    tool_name=tool_instance.identity.name,
                    parameters={**tool_instance.runtime_parameters, **tool_call_args},
                )
                result = ""
                for tool_invoke_response in tool_invoke_responses:
                    if tool_invoke_response.type == ToolInvokeMessage.MessageType.TEXT:
                        result += cast(
                            ToolInvokeMessage.TextMessage, tool_invoke_response.message
                        ).text
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.LINK
                    ):
                        result += (
                            f"result link: {cast(ToolInvokeMessage.TextMessage, tool_invoke_response.message).text}."
                            + " please tell user to check it."
                        )
                    elif tool_invoke_response.type in {
                        ToolInvokeMessage.MessageType.IMAGE_LINK,
                        ToolInvokeMessage.MessageType.IMAGE,
                    }:
                        result += (
                            "image has been created and sent to user already, "
                            + "you do not need to create it, just tell the user to check it now."
                        )
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.JSON
                    ):
                        text = json.dumps(
                            cast(
                                ToolInvokeMessage.JsonMessage,
                                tool_invoke_response.message,
                            ).json_object,
                            ensure_ascii=False,
                        )
                        result += f"tool response: {text}."
                    else:
                        result += f"tool response: {tool_invoke_response.message!r}."

                tool_response = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": result,
                }
        yield self.create_text_message(result)

    def _convert_tool_to_prompt_message_tool(
        self, tool: ToolEntity
    ) -> PromptMessageTool:
        """
        convert tool to prompt message tool
        """
        message_tool = PromptMessageTool(
            name=tool.identity.name,
            description=tool.description.llm if tool.description else "",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )

        parameters = tool.parameters
        for parameter in parameters:
            if parameter.form != ToolParameter.ToolParameterForm.LLM:
                continue

            parameter_type = parameter.type
            if parameter.type in {
                ToolParameter.ToolParameterType.FILE,
                ToolParameter.ToolParameterType.FILES,
            }:
                continue
            enum = []
            if parameter.type == ToolParameter.ToolParameterType.SELECT:
                enum = (
                    [option.value for option in parameter.options]
                    if parameter.options
                    else []
                )

            message_tool.parameters["properties"][parameter.name] = {
                "type": parameter_type,
                "description": parameter.llm_description or "",
            }

            if len(enum) > 0:
                message_tool.parameters["properties"][parameter.name]["enum"] = enum

            if parameter.required:
                message_tool.parameters["required"].append(parameter.name)

        return message_tool

    def check_tool_calls(self, llm_result_chunk: LLMResultChunk) -> bool:
        """
        Check if there is any tool call in llm result chunk
        """
        return bool(llm_result_chunk.delta.message.tool_calls)

    def extract_tool_calls(
        self, llm_result_chunk: LLMResultChunk
    ) -> list[tuple[str, str, dict[str, Any]]]:
        """
        Extract tool calls from llm result chunk

        Returns:
            List[Tuple[str, str, Dict[str, Any]]]: [(tool_call_id, tool_call_name, tool_call_args)]
        """
        tool_calls = []
        for prompt_message in llm_result_chunk.delta.message.tool_calls:
            args = {}
            if prompt_message.function.arguments != "":
                args = json.loads(prompt_message.function.arguments)

            tool_calls.append(
                (
                    prompt_message.id,
                    prompt_message.function.name,
                    args,
                )
            )

        return tool_calls
</code>
</ツールの呼び出し>

<完全な機能コード例>
モデルの呼び出し、ツールの呼び出し、および複数ターンのログ出力機能を含む、完全なプラグインコードの例：
<code>
import json
import time
from collections.abc import Generator
from typing import Any, cast

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig, LLMResult, LLMResultChunk
from dify_plugin.entities.model.message import (
    PromptMessageTool,
    UserPromptMessage,
)
from dify_plugin.entities.tool import ToolInvokeMessage, ToolParameter, ToolProviderType
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity
from pydantic import BaseModel

class BasicParams(BaseModel):
    maximum_iterations: int
    model: AgentModelConfig
    tools: list[ToolEntity]
    query: str

class BasicAgentAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        params = BasicParams(**parameters)
        function_call_round_log = self.create_log_message(
            label="Function Call Round1 ",
            data={},
            metadata={},
        )
        yield function_call_round_log
        model_started_at = time.perf_counter()
        model_log = self.create_log_message(
            label=f"{params.model.model} Thought",
            data={},
            metadata={"start_at": model_started_at, "provider": params.model.provider},
            status=ToolInvokeMessage.LogMessage.LogStatus.START,
            parent=function_call_round_log,
        )
        yield model_log
        chunks: Generator[LLMResultChunk, None, None] | LLMResult = (
            self.session.model.llm.invoke(
                model_config=LLMModelConfig(**params.model.model_dump(mode="json")),
                prompt_messages=[UserPromptMessage(content=params.query)],
                tools=[
                    self._convert_tool_to_prompt_message_tool(tool)
                    for tool in params.tools
                ],
                stop=params.model.completion_params.get("stop", [])
                if params.model.completion_params
                else [],
                stream=True,
            )
        )
        response = ""
        tool_calls = []
        tool_instances = (
            {tool.identity.name: tool for tool in params.tools} if params.tools else {}
        )
        tool_call_names = ""
        tool_call_inputs = ""
        for chunk in chunks:
            # ツール呼び出しがあるか確認
            if self.check_tool_calls(chunk):
                tool_calls = self.extract_tool_calls(chunk)
                tool_call_names = ";".join([tool_call[1] for tool_call in tool_calls])
                try:
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls},
                        ensure_ascii=False,
                    )
                except json.JSONDecodeError:
                    # エンコードエラーを避けるため、asciiを保証
                    tool_call_inputs = json.dumps(
                        {tool_call[1]: tool_call[2] for tool_call in tool_calls}
                    )
                print(tool_call_names, tool_call_inputs)
            if chunk.delta.message and chunk.delta.message.content:
                if isinstance(chunk.delta.message.content, list):
                    for content in chunk.delta.message.content:
                        response += content.data
                        print(content.data, end="", flush=True)
                else:
                    response += str(chunk.delta.message.content)
                    print(str(chunk.delta.message.content), end="", flush=True)

            if chunk.delta.usage:
                # モデルを使用する
                usage = chunk.delta.usage

        yield self.finish_log_message(
            log=model_log,
            data={
                "output": response,
                "tool_name": tool_call_names,
                "tool_input": tool_call_inputs,
            },
            metadata={
                "started_at": model_started_at,
                "finished_at": time.perf_counter(),
                "elapsed_time": time.perf_counter() - model_started_at,
                "provider": params.model.provider,
            },
        )
        yield self.create_text_message(
            text=f"{response or json.dumps(tool_calls, ensure_ascii=False)}\n"
        )
        result = ""
        for tool_call_id, tool_call_name, tool_call_args in tool_calls:
            tool_instance = tool_instances[tool_call_name]
            tool_invoke_responses = self.session.tool.invoke(
                provider_type=ToolProviderType.BUILT_IN,
                provider=tool_instance.identity.provider,
                tool_name=tool_instance.identity.name,
                parameters={**tool_instance.runtime_parameters, **tool_call_args},
            )
            if not tool_instance:
                tool_invoke_responses = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": f"there is not a tool named {tool_call_name}",
                }
            else:
                # ツールを呼び出す
                tool_invoke_responses = self.session.tool.invoke(
                    provider_type=ToolProviderType.BUILT_IN,
                    provider=tool_instance.identity.provider,
                    tool_name=tool_instance.identity.name,
                    parameters={**tool_instance.runtime_parameters, **tool_call_args},
                )
                result = ""
                for tool_invoke_response in tool_invoke_responses:
                    if tool_invoke_response.type == ToolInvokeMessage.MessageType.TEXT:
                        result += cast(
                            ToolInvokeMessage.TextMessage, tool_invoke_response.message
                        ).text
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.LINK
                    ):
                        result += (
                            f"result link: {cast(ToolInvokeMessage.TextMessage, tool_invoke_response.message).text}."
                            + " please tell user to check it."
                        )
                    elif tool_invoke_response.type in {
                        ToolInvokeMessage.MessageType.IMAGE_LINK,
                        ToolInvokeMessage.MessageType.IMAGE,
                    }:
                        result += (
                            "image has been created and sent to user already, "
                            + "you do not need to create it, just tell the user to check it now."
                        )
                    elif (
                        tool_invoke_response.type == ToolInvokeMessage.MessageType.JSON
                    ):
                        text = json.dumps(
                            cast(
                                ToolInvokeMessage.JsonMessage,
                                tool_invoke_response.message,
                            ).json_object,
                            ensure_ascii=False,
                        )
                        result += f"tool response: {text}."
                    else:
                        result += f"tool response: {tool_invoke_response.message!r}."

                tool_response = {
                    "tool_call_id": tool_call_id,
                    "tool_call_name": tool_call_name,
                    "tool_response": result,
                }
        yield self.create_text_message(result)

    def _convert_tool_to_prompt_message_tool(
        self, tool: ToolEntity
    ) -> PromptMessageTool:
        """
        convert tool to prompt message tool
        """
        message_tool = PromptMessageTool(
            name=tool.identity.name,
            description=tool.description.llm if tool.description else "",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )

        parameters = tool.parameters
        for parameter in parameters:
            if parameter.form != ToolParameter.ToolParameterForm.LLM:
                continue

            parameter_type = parameter.type
            if parameter.type in {
                ToolParameter.ToolParameterType.FILE,
                ToolParameter.ToolParameterType.FILES,
            }:
                continue
            enum = []
            if parameter.type == ToolParameter.ToolParameterType.SELECT:
                enum = (
                    [option.value for option in parameter.options]
                    if parameter.options
                    else []
                )

            message_tool.parameters["properties"][parameter.name] = {
                "type": parameter_type,
                "description": parameter.llm_description or "",
            }

            if len(enum) > 0:
                message_tool.parameters["properties"][parameter.name]["enum"] = enum

            if parameter.required:
                message_tool.parameters["required"].append(parameter.name)

        return message_tool

    def check_tool_calls(self, llm_result_chunk: LLMResultChunk) -> bool:
        """
        Check if there is any tool call in llm result chunk
        """
        return bool(llm_result_chunk.delta.message.tool_calls)

    def extract_tool_calls(
        self, llm_result_chunk: LLMResultChunk
    ) -> list[tuple[str, str, dict[str, Any]]]:
        """
        Extract tool calls from llm result chunk

        Returns:
            List[Tuple[str, str, Dict[str, Any]]]: [(tool_call_id, tool_call_name, tool_call_args)]
        """
        tool_calls = []
        for prompt_message in llm_result_chunk.delta.message.tool_calls:
            args = {}
            if prompt_message.function.arguments != "":
                args = json.loads(prompt_message.function.arguments)

            tool_calls.append(
                (
                    prompt_message.id,
                    prompt_message.function.name,
                    args,
                )
            )

        return tool_calls
</code>
</完全な機能コード例>

#### 3. プラグインのデバッグ
プラグインの設定ファイルと機能コードを記述したら、プラグインのディレクトリ内で python -m main コマンドを実行してプラグインを再起動します。次に、プラグインが正常に動作するかどうかをテストする必要があります。Difyのリモートデバッグ機能を利用するには、「プラグイン管理」にアクセスしてデバッグキーとリモートサーバーのアドレスを取得してください。

プラグインプロジェクトに戻り、.env.example ファイルをコピーして .env にリネームします。そして、取得したリモートサーバーのアドレスとデバッグキーを、.envファイルの REMOTE_INSTALL_HOST および REMOTE_INSTALL_KEY パラメータにそれぞれ入力します。

<code>
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=localhost
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
</code>

python -m main コマンドを実行してプラグインを起動します。プラグインページで、プラグインがワークスペースにインストールされたことを確認できます。このプラグインは、他のチームメンバーも利用可能です。

#### プラグインのパッケージ化（オプション）
プラグインが正常に動作することを確認したら、以下のコマンドラインツールを使用してプラグインをパッケージ化し、名前を付けることができます。実行後、現在のフォルダに google.difypkg ファイルが生成されます。これが最終的なプラグインパッケージです。

<code>
dify plugin package ./basic_agent/
</code>

おめでとうございます！これで、ツールタイプのプラグインの開発、デバッグ、パッケージ化の全プロセスが完了しました。

#### プラグインの公開（オプション）
作成したプラグインは、Dify Plugins コードリポジトリにアップロードして公開できます。アップロードする前に、プラグインがプラグイン公開規約に準拠していることをご確認ください。審査に合格すると、コードはメインブランチにマージされ、Dify Marketplaceに自動的に公開されます。

#### さらに詳しく
複雑なタスクでは、複数回の思考とツール呼び出しが必要になることがよくあります。より高度なタスク処理を実現するために、通常は反復実行戦略が採用されます。つまり、「モデル呼び出し → ツール呼び出し」という流れを、タスクが完了するか、設定された最大反復回数に達するまで繰り返します。

このプロセスにおいて、プロンプト管理は非常に重要です。モデル入力を効率的に整理し、動的に調整するために、プラグイン内のFunction Calling機能の実装コードを参照し、標準化された方法でモデルが外部ツールを呼び出し、その結果を処理する方法を理解することを推奨します。

### 拡張機能型プラグイン
このドキュメントでは、Extensionタイプのプラグインを迅速に開発し、プラグイン開発の基本的な流れを理解するのに役立つように解説します。

#### 事前準備
- Difyプラグインの足場ツール
- Python環境、バージョン番号 ≥ 3.12

プラグイン開発の足場ツールの準備方法については、開発ツールの初期化を参照してください。

#### 新規プロジェクトの作成
現在のパスで、足場コマンドラインツールを実行し、新しいDifyプラグインプロジェクトを作成します。

<code>
./dify-plugin-darwin-arm64 plugin init
</code>

このバイナリファイルをdifyにリネームし、/usr/local/binパスにコピーした場合、以下のコマンドを実行して新しいプラグインプロジェクトを作成できます。

<code>
dify plugin init
</code>

#### プラグイン情報の入力
表示される指示に従って、プラグイン名、作者情報、プラグインの説明を設定してください。チームで共同作業する場合は、作者を組織名にすることも可能です。

プラグイン名の長さは1〜128文字で、文字、数字、ダッシュ、アンダースコアのみを使用できます。

入力が完了したら、プラグイン開発言語の選択でPythonを選択してください。

#### プラグインタイプの選択とプロジェクトテンプレートの初期化
足場ツール内のすべてのテンプレートには、完全なコードプロジェクトが用意されています。このドキュメントでは、例としてExtensionタイプのプラグインテンプレートを使用します。プラグインに精通している開発者であれば、テンプレートを使用せずに、APIドキュメントを参照して様々なタイプのプラグイン開発を進めることができます。

#### プラグイン権限の設定
プラグインがDifyメインプラットフォームに正常に接続するためには、Difyメインプラットフォームの権限を読み取る必要があります。このサンプルプラグインには、以下の権限を付与してください。

- ツール
- LLM
- アプリ
- 永続ストレージを有効にし、デフォルトサイズのストレージを割り当てる
- エンドポイントの登録を許可する

ターミナル内で方向キーを使って権限を選択し、「Tab」キーで権限を付与します。

すべての権限項目をチェックした後、Enterキーを押してプラグインの作成を完了します。システムが自動的にプラグインのプロジェクトコードを生成します。


プラグインの基本ファイル構造は以下の通りです。

<path>
.
├── GUIDE.md
├── README.md
├── _assets
│   └── icon.svg
├── endpoints
│   ├── your-project.py
│   └── your-project.yaml
├── group
│   └── your-project.yaml
├── main.py
├── manifest.yaml
└── requirements.txt
</path>

- GUIDE.md: プラグインの作成プロセスを説明する簡単なチュートリアルです。
- README.md: 現在のプラグインに関する情報です。このプラグインの概要や使用方法をこのファイルに記述する必要があります。
- _assets: 現在のプラグインに関連するすべてのマルチメディアファイルを保存します。
- endpoints: CLIのガイドに従って作成されるExtensionタイプのプラグインテンプレートです。このディレクトリには、すべてのエンドポイントの機能実装コードが格納されています。
- group: 秘密鍵のタイプ、多言語設定、API定義ファイルのパスを指定します。
- main.py: プロジェクト全体のエントリポイントとなるファイルです。
- manifest.yaml: プラグインの基本設定ファイルです。このプラグインに必要な権限、拡張機能の種類などの設定情報が含まれています。
- requirements.txt: Python環境の依存関係を記述します。

#### プラグインの開発
##### 1. プラグインのリクエストエンドポイントの定義
endpoints/test_plugin.yamlを編集し、以下のコードを参考に変更してください。

<code>
path: "/neko"
method: "GET"
extra:
  python:
    source: "endpoints/test_plugin.py"
</code>

このコードは、プラグインのエントリパスを/neko、リクエストメソッドをGETタイプとして定義するものです。プラグインの機能実装コードは、endpoints/test_plugin.pyファイルに記述します。

##### 2. プラグイン機能の作成
プラグインの機能：プラグインサービスをリクエストし、猫の情報を出力します。

プラグインの機能実装コードをendpoints/test_plugin.pyファイルに記述します。以下のサンプルコードを参考にしてください。

<code>
from typing import Mapping
from werkzeug import Request, Response
from flask import Flask, render_template_string
from dify_plugin import Endpoint

app = Flask(__name__)

class NekoEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        ascii_art = '''
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬜️⬜️⬜️⬜️⬜⬜️⬜️️
🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️⬜️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧🥧💟💟💟💟💟💟💟💟💟💟💟💟💟🥧🥧🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧💟💟💟💟💟💟🍓💟💟🍓💟💟💟💟💟🥧🥧⬛️⬜️⬜️⬜️⬜️⬜️️
🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥⬛🥧💟💟🍓💟💟💟💟💟💟💟💟💟💟💟💟💟💟🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟💟⬛️⬛️💟💟🍓💟💟🥧⬛️⬜️⬛️️⬛️️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫⬛💟💟💟💟🥧⬛️⬛️🌫🌫⬛⬜️️
🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟨🟧⬛️⬛️⬛️⬛️🟧🟧⬛️🥧💟💟💟💟💟💟🍓💟💟⬛️🌫🌫🌫⬛💟💟💟🥧⬛️🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️🌫🌫⬛️⬛️🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫🌫🌫⬛️⬛️⬛️⬛️🌫🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️⬛️🌫🌫⬛️⬛️⬛️🥧💟💟💟🍓💟💟💟💟💟⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛⬜️️
🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟨🟨⬛⬛️🌫🌫⬛️⬛️🥧💟💟💟💟💟💟💟🍓⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️🌫🌫⬛️🥧💟🍓💟💟💟💟💟💟⬛️🌫🌫🌫⬜️⬛️🌫🌫🌫🌫🌫⬜️⬛️🌫🌫⬛️
️🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️⬛️⬛️🥧💟💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️🌫🌫🌫⬛️🌫⬛️⬛️🌫🌫⬛️
🟦🟦🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦🟦🟩🟩🟩🟩🟩🟩⬛️⬛️🥧💟💟💟💟💟🍓💟💟⬛🌫🟥🟥🌫🌫🌫🌫🌫🌫🌫🌫🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧💟🍓💟💟💟💟💟⬛️🌫🟥🟥🌫⬛️🌫🌫⬛️🌫🌫⬛️🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧🥧💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️🌫🌫⬛️⬜️
🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟦🟦🟦🟦🟦🟦⬛️⬛️⬛️🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫⬛️⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️⬜️⬛️🌫🌫⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️
⬜️⬜️🟪🟪🟪🟪🟪🟪🟪🟪⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟪🟪🟪🟪🟪⬛️⬛️⬛️⬛⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️️
        '''
        ascii_art_lines = ascii_art.strip().split('\n')
        with app.app_context():
            return Response(render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: white;
                overflow: hidden;
                margin: 0;
                padding: 0;
            }
            #ascii-art {
                font-family: monospace;
                white-space: pre;
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                display: inline-block;
                font-size: 16px;
                line-height: 1;
            }
        </style>
    </head>
    <body>
        <div id="ascii-art"></div>
        <script>
            var asciiArtLines = {{ ascii_art_lines | tojson }};
            var asciiArtDiv = document.getElementById("ascii-art");
            var index = 0;
            function displayNextLine() {
                if (index < asciiArtLines.length) {
                    var line = asciiArtLines[index];
                    var lineElement = document.createElement("div");
                    lineElement.innerHTML = line;
                    asciiArtDiv.appendChild(lineElement);
                    index++;
                    setTimeout(displayNextLine, 100);
                } else {
                    animateCat();
                }
            }
            function animateCat() {
                var pos = 0;
                var screenWidth = window.innerWidth;
                var catWidth = asciiArtDiv.offsetWidth;
                function move() {
                    asciiArtDiv.style.left = pos + "px";
                    pos += 2;
                    if (pos > screenWidth) {
                        pos = -catWidth;
                    }
                    requestAnimationFrame(move);
                }
                move();
            }
            displayNextLine();
        </script>
    </body>
    </html>
        ''', ascii_art_lines=ascii_art_lines), status=200, content_type="text/html")
</code>

このコードを実行する前に、まず以下のPythonの依存パッケージをインストールする必要があります。

<code>
pip install werkzeug
pip install flask
pip install dify-plugin
<code>

#### プラグインのデバッグ
次に、プラグインが正常に動作するかどうかをテストします。Difyはリモートデバッグ機能を提供しており、「プラグイン管理」ページでデバッグキーとリモートサーバーのアドレスを取得できます。

プラグインのプロジェクトに戻り、.env.exampleファイルをコピーして.envにリネームします。そして、取得したリモートサーバーのアドレスやデバッグキーなどの情報を.envファイルに記入してください。

.envファイルの内容：
<code>
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
</code>

python -m mainコマンドを実行してプラグインを起動します。プラグインページで、このプラグインがワークスペースにインストールされたことを確認できます。他のチームメンバーもこのプラグインにアクセス可能です。

プラグイン内に新しいエンドポイントを追加し、名前やapi_keyなどの情報を任意で入力します。自動生成されたURLにアクセスすると、プラグインが提供するウェブサービスが表示されます。


#### プラグインのパッケージ化
プラグインが正常に動作することを確認したら、以下のコマンドラインツールを使用してプラグインをパッケージ化し、名前を付けることができます。実行後、現在のフォルダにneko.difypkgというファイルが生成されます。このファイルが最終的なプラグインパッケージです。

<code>
dify-plugin package ./neko
</code>

おめでとうございます！これで、プラグインの開発、テスト、パッケージ化の全工程が完了しました。

#### プラグインの公開
作成したプラグインは、Dify Plugins コードリポジトリにアップロードして公開できます。アップロードする前に、プラグインがプラグイン公開仕様に準拠していることを確認してください。審査に合格すると、コードはメインブランチにマージされ、Dify Marketplaceに自動的に公開されます。

### バンドル
バンドルプラグインパッケージは、複数のプラグインをまとめたものです。複数のプラグインを一つのパッケージにまとめることで、プラグインの一括インストールを可能にし、より高度な機能を提供します。

Dify CLIツールを使用すると、複数のプラグインをバンドルとしてパッケージ化できます。バンドルプラグインパッケージには、以下の3つのタイプがあります。

- Marketplace タイプ：プラグインのIDとバージョン情報を保持します。インポート時には、Dify Marketplaceから該当するプラグインパッケージをダウンロードします。
- GitHub タイプ：GitHubリポジトリのアドレス、リリースバージョン番号、アセットファイル名を保持します。インポート時に、Difyは該当するGitHubリポジトリにアクセスしてプラグインパッケージをダウンロードします。
- Package タイプ：プラグインパッケージをバンドル内に直接格納します。参照元は保持されませんが、バンドルパッケージのサイズが大きくなる可能性があります。

#### 事前準備
- Difyプラグインのひな形ツール
- Python環境（バージョン3.10以上）

プラグイン開発のひな形ツールを準備する方法の詳細については、「開発ツールの初期化」を参照してください。

#### バンドルプロジェクトの作成
現在のディレクトリで、ひな形コマンドラインツールを実行し、新しいプラグインパッケージプロジェクトを作成します。

<code>
./dify-plugin-darwin-arm64 bundle init
</code>

このバイナリファイルを dify にリネームし、/usr/local/bin ディレクトリにコピーした場合、次のコマンドを実行して新しいプラグインプロジェクトを作成できます。

<code>
dify bundle init
</code>

#### 1. プラグイン情報の入力
プロンプトに従って、プラグイン名、作成者情報、プラグインの説明を設定します。チームで共同作業している場合は、作成者に組織名を記入することもできます。

名前は1〜128文字で、文字、数字、ダッシュ、アンダースコアのみを使用できます。

情報を入力してEnterキーを押すと、バンドルプラグインプロジェクトのディレクトリが自動的に作成されます。

#### 2. 依存関係の追加
- マーケットプレイス(Marketplace)
次のコマンドを実行します。
<code>
dify-plugin bundle append marketplace . --marketplace_pattern=langgenius/openai:0.0.1
</code>

ここで、marketplace_pattern は、Marketplaceでのプラグインの参照であり、形式は 組織名/プラグイン名:バージョン番号 です。

- Github
次のコマンドを実行します。

<code>
dify-plugin bundle append github . --repo_pattern=langgenius/openai:0.0.1/openai.difypkg
</code>

ここで、repo_pattern は、GitHubでのプラグインの参照であり、形式は 組織名/リポジトリ名:リリース/添付ファイル名 です。

- パッケージ(package)
次のコマンドを実行します。
<code>
dify-plugin bundle append package . --package_path=./openai.difypkg
</code>

ここで、package_path は、プラグインパッケージのディレクトリです。

#### バンドルプロジェクトのパッケージ化
次のコマンドを実行して、バンドルプラグインをパッケージ化します。

<code>
dify-plugin bundle package ./bundle
</code>

コマンドを実行すると、現在のディレクトリに bundle.difybndl ファイルが自動的に作成されます。このファイルが最終的なパッケージ結果です。

## プラグインのデバッグ方法
プラグインの開発が完了したら、次は正常に動作するかどうかをテストしましょう。Difyはリモートデバッグ機能を提供しており、「プラグイン管理」ページでデバッグキーとリモートサーバーアドレスを取得できます。

プラグインのプロジェクトに戻り、.env.exampleファイルをコピーして.envにリネームします。そして、取得したリモートサーバーアドレスやデバッグキーなどの情報を入力してください。

.envファイル
<code>
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
</code>
python -m mainコマンドを実行してプラグインを起動します。プラグインページで、Workspaceにインストールされたことを確認できます。他のチームメンバーもこのプラグインを利用可能です。

# プラグイン管理方法
このガイドは、ワークスペースの所有者や管理者向けに、プラグインの権限を設定し、管理する方法を詳しく説明します。プラグインの権限を管理することで、どのユーザーがプラグインに関連する操作を行えるかを定めることができます。

## プラグイン権限の設定
チームの所有者や管理者は、Difyプラットフォームのホームページ右上にある 「プラグイン」 ページから、次のプラグイン権限を設定できます：

- プラグインのインストールと管理
この権限により、誰がプラグインをインストールや管理できるかを決めます。オプションには以下があります：

-- Everyone（全員）: ワークスペース内の全てのユーザーがプラグインをインストールや管理できる
-- Admins（管理者）: ワークスペースの管理者だけがプラグインをインストールや管理できる
-- No one（無人）: 誰もプラグインをインストールや管理できない

- プラグインのデバッグの権限
この権限により、誰がプラグインのデバッグを行えるかを決めます。オプションには以下があります：
-- Everyone（全員）: ワークスペース内の全てのユーザーがプラグインをデバッグできる
-- Admins（管理者）: ワークスペースの管理者だけがプラグインをデバッグできる
-- No one（無人）: 誰もプラグインをデバッグできない

## プラグインの更新
Difyプラットフォームの右上にある「プラグイン」ボタンをクリックし、更新が必要なプラグインを選択。その後、プラグインタイトルの隣にある 「アップグレード」 ボタンをクリックしてください。

## プラグインの削除方法
Difyプラットフォームの右上にある「プラグイン」ボタンをクリックし、現在ワークスペースにインストールされているプラグイン一覧を表示します。プラグインの詳細ページで、「削除」アイコンまたは「削除」ボタンをクリックして、プラグインを削除してください。

# スキーマ使用
## Manifest
マニフェストファイル マニフェストファイルとは、プラグインに関する最も基本的な情報を定義するYAML形式のファイルです。プラグイン名、作成者、含まれるツールやモデルなどの情報が含まれます。

このファイルの形式が正しくないと、プラグインの解析とパッケージング処理は失敗します。

### コード例
以下は、マニフェストファイルの簡単な例です。各データ要素の意味と機能については、以下で説明します。他のプラグインコードについては、Githubリポジトリ を参照してください。

<code>
version: 0.0.1
type: "plugin"
author: "Yeuoly"
name: "neko"
label:
  en_US: "Neko"
created_at: "2024-07-12T08:03:44.658609186Z"
icon: "icon.svg"
resource:
  memory: 1048576
  permission:
    tool:
      enabled: true
    model:
      enabled: true
      llm: true
    endpoint:
      enabled: true
    app:
      enabled: true
    storage: 
      enabled: true
      size: 1048576
plugins:
  endpoints:
    - "provider/neko.yaml"
meta:
  version: 0.0.1
  arch:
    - "amd64"
    - "arm64"
  runner:
    language: "python"
    version: "3.10"
    entrypoint: "main"
</code>

### 構造
- version (version、required): プラグインのバージョン
- type (type、required): プラグインの種類。現在はpluginのみをサポートしており、将来的にはbundleをサポート予定
- author (string、required): 作成者。マーケットプレイスでは組織名として扱われます
- label (label、required): 多言語対応の名前
- created_at (RFC3339、required): 作成時間。マーケットプレイスでは現在時刻より後の日時であってはなりません
- icon (アセット、required): アイコンのパス
- resource (object): 必要なリソース設定
    -- memory (int64): 最大メモリ使用量。主にSaaS上のAWS Lambdaリソースリクエストに関連し、単位はバイト
    -- permission (object): 権限設定
        --- tool (object): ツール呼び出しの権限
            ---- enabled (bool)
        --- model (object): モデル呼び出しの権限
            ---- enabled (bool)
            ---- llm (bool)
            ---- text_embedding (bool)
            ---- rerank (bool)
            ---- tts (bool)
            ---- speech2text (bool)
            ---- moderation (bool)
        --- node (object): ノード呼び出しの権限
            ---- enabled (bool)
        --- endpoint (object): エンドポイント登録の権限
            ---- enabled (bool)
        --- app (object): アプリ呼び出しの権限
            ---- enabled (bool)
        --- storage (object): 永続ストレージの権限
            ---- enabled (bool)
            ---- size (int64): 最大許容永続メモリサイズ（バイト単位）
- plugins (object、required): プラグインの機能を定義するYAMLファイルのリスト。プラグインパッケージ内の絶対パスで指定
    -- 形式：
        --- tools (list[string]): 拡張されたツールプロバイダ
        --- models (list[string]): 拡張されたモデルプロバイダ
        --- endpoints (list[string]): 拡張されたエンドポイントプロバイダ
        --- agent_strategies (list[string]): 拡張されたエージェント戦略プロバイダ
    -- 制限：
        --- ツールとモデルの両方を同時に拡張することはできません。
        --- 少なくとも1つの拡張が必要です。
        --- モデルとエンドポイントの両方を同時に拡張することはできません。
        --- 現在、拡張タイプごとに1つのプロバイダのみをサポートしています。
    -- meta (object): メタ情報
        --- version (version、required): マニフェスト形式のバージョン。初期バージョンは0.0.1
        --- arch (list[string]、required): サポートされるアーキテクチャ。現在はamd64とarm64のみ
        --- runner (object、required): ランタイム設定
            ---- language (string): 現在はPythonのみをサポート
            ---- version (string): 言語バージョン。現在は3.12のみをサポート
            ---- entrypoint (string): プログラムのエントリポイント。Pythonの場合はmainである必要があります。


## Endpoint
この記事では、プラグイン内のエンドポイントの構造を説明するために、クイックスタート：レインボーキャットプロジェクトを例として取り上げます。完全なプラグインコードは、Githubで確認できます。

### グループの定義
Endpointグループは、複数のEndpointをまとめたものです。Difyプラグインで新しいEndpointを作成する際には、以下の設定項目を入力する必要があります。

「Endpoint Name」の他に、グループ構成情報を記述することで、新しいフォーム項目を追加できます。保存すると、同じ構成情報を使用する複数のインターフェースが表示されるようになります。

### 構造
- settings (map[string] ProviderConfig): エンドポイントの設定定義
- endpoints (list[string], required): 特定のendpointインターフェース定義を指定します。

<code>
settings:
  api_key:
    type: secret-input
    required: true
    label:
      en_US: API key
      zh_Hans: API key
      ja_Jp: API key
      pt_BR: API key
    placeholder:
      en_US: Please input your API key
      zh_Hans: 请输入你的 API key
      ja_Jp: あなたの API key を入れてください
      pt_BR: Por favor, insira sua chave API
endpoints:
  - endpoints/duck.yaml
  - endpoints/neko.yaml
</code>

### インターフェース定義
- path (string): werkzeugのインターフェース標準に従います。
- method (string): インターフェースのメソッド。HEAD GET POST PUT DELETE OPTIONSのみをサポートします。
- extra (object): 基本情報以外の設定情報
    -- python (object)
        --- source (string): このインターフェースを実装するソースコード

<code>
path: "/duck/<app_id>"
method: "GET"
extra:
  python:
    source: "endpoints/duck.py"
</code>

### エンドポイントの実装
dify_plugin.Endpointを継承したサブクラスを実装し、_invokeメソッドを実装する必要があります。

- 入力パラメータ
    -- r (Request): werkzeugからのリクエストオブジェクト
    -- values (Mapping): パスから解析されたパスパラメータ
    -- settings (Mapping): このエンドポイントの設定情報
- 戻り値
    -- werkzeugからのレスポンスオブジェクト。ストリーミングでの応答をサポートします。
    -- 直接的な文字列の戻り値はサポートしません。

コード例:
<code>
import json
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class Duck(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        app_id = values["app_id"]
        def generator():
            yield f"{app_id} <br>"
        return Response(generator(), status=200, content_type="text/html")
</code>

## Tool(ツール)
詳細なインターフェースドキュメントを読む前に、クイックスタート：ツール を参照し、Difyプラグインにおけるツールの利用プロセスについて、概要を把握しておいてください。

### データ構造
#### メッセージの出力
Difyは、text、links、images、file BLOBs、JSONといった複数のメッセージタイプをサポートしています。様々なインターフェースを通じて、これらの異なるタイプのメッセージを出力できます。

デフォルトでは、ワークフロー内でツールが出力する際には、files、text、jsonという3つの固定の変数が用意されています。これらの変数にデータを設定するには、以下のメソッドを使用します。

例えば、create_image_messageを使用すると、画像を出力できます。また、ツールはワークフロー内で参照しやすいように、カスタムの出力変数もサポートしています。

#### 画像URL
画像のURLを渡すだけで、Difyが自動的に画像をダウンロードし、ユーザーに送信します。

<code>
def create_image_message(self, image: str) -> ToolInvokeMessage:
    pass
</code>

#### リンク
リンクを出力するには、このインターフェースを使用します。
<code>
def create_link_message(self, link: str) -> ToolInvokeMessage:
    pass
</code>

#### テキスト
テキストメッセージを出力するには、このインターフェースを使用します。

<code>
def create_text_message(self, text: str) -> ToolInvokeMessage:
    pass
</code>

#### ファイル
生のファイルデータ（画像、音声、動画、PPT、Word、Excelなど）を出力するには、このインターフェースを使用します。

- blob: バイト形式の生ファイルデータ
- meta: ファイルのメタデータです。mime_typeを指定することで、ファイルの種類を明示できます。指定しない場合は、Difyがデフォルトでoctet/streamを使用します。

<code>
def create_blob_message(self, blob: bytes, meta: dict = None) -> ToolInvokeMessage:
    pass
</code>

#### JSON
フォーマットされたJSONを出力するには、このインターフェースを使用します。通常、ワークフロー内のノード間でデータをやり取りする際に使用されます。多くの大規模言語モデルは、エージェントモードでJSON形式のデータを読み取り、理解できます。

<code>
def create_json_message(self, json: dict) -> ToolInvokeMessage:
    pass
</code>

#### 変数
ストリーミングではない出力変数を設定するには、このインターフェースを使用します。後から設定された値は、以前の設定値を上書きします。

<code>
def create_variable_message(self, variable_name: str, variable_value: Any) -> ToolInvokeMessage:
    pass
</code>

#### ストリーミング変数
テキストをタイプライターのように表示するには、ストリーミング変数を使用します。チャットフローアプリケーションの応答ノードでこの変数を参照すると、テキストがタイプライター効果で表示されます。現在、文字列データのみをサポートしています。

<code>
def create_stream_variable_message(
    self, variable_name: str, variable_value: str
) -> ToolInvokeMessage:
</code>

#### 出力変数の定義
ワークフロー内でツールの出力変数を参照するには、事前に出力される可能性のある変数を定義しておく必要があります。Difyプラグインは、json_schema形式での出力変数定義をサポートしています。以下に設定例を示します。

<code>
identity:
  author: author
  name: tool
  label:
    en_US: label
    zh_Hans: 标签
    ja_JP: レベル
    pt_BR: etiqueta
description:
  human:
    en_US: description
    zh_Hans: 描述
    ja_JP: 説明
    pt_BR: descrição
  llm: description
output_schema:
  type: object
  properties:
    name:
      type: string
</code>

この例では、ワークフロー内で参照できる name フィールドを含む output_schema を持つシンプルなツールを定義しています。実際に使用するには、ツールの実装コード内で変数を設定する必要があることに注意してください。そうしないと、None が設定されます。

## エージェント（Agent）
### エージェント戦略の概要
エージェント戦略とは、標準的な入力コンテンツと出力形式を定義する拡張可能なテンプレートです。特定のエージェント戦略インターフェースを開発することで、CoT（Chain of Thought：思考の連鎖）、ToT（Tree of Thought：思考の木）、GoT（Graph of Thought：思考のグラフ）、BoT（Backbone of Thought：思考のバックボーン）といった様々なエージェント戦略を実装したり、Semantic Kernel のような複雑な戦略を実現したりできます。

### マニフェストへのフィールド追加
プラグインにエージェント戦略を追加するには、manifest.yamlファイルにplugins.agent_strategiesフィールドを追加し、エージェントプロバイダーを定義します。以下にコード例を示します。

<code>
version: 0.0.2
type: plugin
author: "langgenius"
name: "agent"
plugins:
  agent_strategies:
    - "provider/agent.yaml"
</code>

マニフェストファイル内の関連性のないフィールドは省略されています。詳細なマニフェスト形式については、Manifestを参照してください。

### エージェントプロバイダーの定義
基本的なエージェントプロバイダー情報を含むagent.yamlファイルを作成します。

<code>
identity:
  author: langgenius
  name: agent
  label:
    en_US: Agent
    zh_Hans: Agent
    pt_BR: Agent
  description:
    en_US: Agent
    zh_Hans: Agent
    pt_BR: Agent
  icon: icon.svg
strategies:
  - strategies/function_calling.yaml
</code>

### エージェント戦略の定義と実装
#### 定義
エージェント戦略のコードを定義するために、function_calling.yamlファイルを作成します。

<code>
identity:
  name: function_calling
  author: Dify
  label:
    en_US: FunctionCalling
    zh_Hans: FunctionCalling
    pt_BR: FunctionCalling
description:
  en_US: Function Calling is a basic strategy for agent, model will use the tools provided to perform the task.
parameters:
  - name: model
    type: model-selector
    scope: tool-call&llm
    required: true
    label:
      en_US: Model
  - name: tools
    type: array[tools]
    required: true
    label:
      en_US: Tools list
  - name: query
    type: string
    required: true
    label:
      en_US: Query
  - name: max_iterations
    type: number
    required: false
    default: 5
    label:
      en_US: Max Iterations
    max: 50
    min: 1
extra:
  python:
    source: strategies/function_calling.py
</code>

このコード形式はToolの標準形式に似ており、最も基本的なエージェント戦略を実装するために、model、tools、query、max_iterationsの4つのパラメーターを定義しています。これにより、ユーザーは以下のことが可能になります。

- 使用するモデルを選択する
- 利用するツールを選択する
- 最大反復回数を設定する
- エージェントの実行を開始するためのクエリを入力する

これらのパラメーターはすべて連携して、エージェントがタスクを処理し、選択されたツールやモデルとどのように対話するかを定義します。

#### 機能実装
##### パラメーターの取得

前述の4つのパラメーターに基づき、モデルタイプのパラメーターはmodel-selector、ツールタイプのパラメーターは特別なarray[tools]です。取得したパラメーターは、SDKに組み込まれているAgentModelConfigとlist[ToolEntity]を使用して変換できます。

<code>
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity

class FunctionCallingParams(BaseModel):
    query: str
    model: AgentModelConfig
    tools: list[ToolEntity] | None
    maximum_iterations: int = 3
    
 class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        fc_params = FunctionCallingParams(**parameters)
</code>

##### モデルの呼び出し
特定モデルの呼び出しは、エージェントプラグインの不可欠な機能です。SDKのsession.model.invoke()関数を使用してモデルを呼び出します。必要な入力パラメーターはモデルから取得できます。

モデルを呼び出すメソッドの例：
<code>
def invoke(
        self,
        model_config: LLMModelConfig,
        prompt_messages: list[PromptMessage],
        tools: list[PromptMessageTool] | None = None,
        stop: list[str] | None = None,
        stream: bool = True,
    ) -> Generator[LLMResultChunk, None, None] | LLMResult:
</code>

モデル情報（model_config）、プロンプト情報（prompt_messages）、ツール情報（tools）を渡す必要があります。prompt_messagesパラメーターは以下のコード例を参照できますが、tool_messagesには特定の変換が必要です。

モデル呼び出しのコード例を参照してください。

<code>
from collections.abc import Generator
from typing import Any

from pydantic import BaseModel

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.model.message import (
    PromptMessageTool,
    SystemPromptMessage,
    UserPromptMessage,
)
from dify_plugin.entities.tool import ToolParameter
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity

class FunctionCallingParams(BaseModel):
    query: str
    instruction: str | None
    model: AgentModelConfig
    tools: list[ToolEntity] | None
    maximum_iterations: int = 3

class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        # init params
        fc_params = FunctionCallingParams(**parameters)
        query = fc_params.query
        model = fc_params.model
        stop = fc_params.model.completion_params.get("stop", []) if fc_params.model.completion_params else []
        prompt_messages = [
            SystemPromptMessage(content="your system prompt message"),
            UserPromptMessage(content=query),
        ]
        tools = fc_params.tools
        prompt_messages_tools = self._init_prompt_tools(tools)

        # invoke llm
        chunks = self.session.model.llm.invoke(
            model_config=LLMModelConfig(**model.model_dump(mode="json")),
            prompt_messages=prompt_messages,
            stream=True,
            stop=stop,
            tools=prompt_messages_tools,
        )

    def _init_prompt_tools(self, tools: list[ToolEntity] | None) -> list[PromptMessageTool]:
        """
        Init tools
        """

        prompt_messages_tools = []
        for tool in tools or []:
            try:
                prompt_tool = self._convert_tool_to_prompt_message_tool(tool)
            except Exception:
                # api tool may be deleted
                continue

            # save prompt tool
            prompt_messages_tools.append(prompt_tool)

        return prompt_messages_tools

    def _convert_tool_to_prompt_message_tool(self, tool: ToolEntity) -> PromptMessageTool:
        """
        convert tool to prompt message tool
        """
        message_tool = PromptMessageTool(
            name=tool.identity.name,
            description=tool.description.llm if tool.description else "",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )

        parameters = tool.parameters
        for parameter in parameters:
            if parameter.form != ToolParameter.ToolParameterForm.LLM:
                continue

            parameter_type = parameter.type
            if parameter.type in {
                ToolParameter.ToolParameterType.FILE,
                ToolParameter.ToolParameterType.FILES,
            }:
                continue
            enum = []
            if parameter.type == ToolParameter.ToolParameterType.SELECT:
                enum = [option.value for option in parameter.options] if parameter.options else []

            message_tool.parameters["properties"][parameter.name] = {
                "type": parameter_type,
                "description": parameter.llm_description or "",
            }

            if len(enum) > 0:
                message_tool.parameters["properties"][parameter.name]["enum"] = enum

            if parameter.required:
                message_tool.parameters["required"].append(parameter.name)

        return message_tool
<code>

##### ツールの呼び出し

ツールの呼び出しも、エージェントプラグインの重要な機能です。ツールを呼び出すには、self.session.tool.invoke()を使用します。
ツールを呼び出すメソッドの例：
<code>
def invoke(
        self,
        provider_type: ToolProviderType,
        provider: str,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]
<code>

必要なパラメーターには、provider_type、provider、tool_name、parametersが含まれます。通常、tool_nameとparametersは関数呼び出し中にLLMによって生成されます。

ツールを呼び出すコード例：
<code>
from dify_plugin.entities.tool import ToolProviderType

class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        fc_params = FunctionCallingParams(**parameters)
        
        # tool_call_name と tool_call_args パラメータはLLMの出力から取得されます。
        tool_instances = {tool.identity.name: tool for tool in fc_params.tools} if fc_params.tools else {}
        tool_instance = tool_instances[tool_call_name]
        tool_invoke_responses = self.session.tool.invoke(
            provider_type=ToolProviderType.BUILT_IN,
            provider=tool_instance.identity.provider,
            tool_name=tool_instance.identity.name,
            # デフォルト値を追加
            parameters={**tool_instance.runtime_parameters, **tool_call_args},
        )
</code>

self.session.tool.invoke()関数の出力はジェネレーターであり、ストリーム解析が必要です。

解析については、以下の関数を参照してください。
<code>
import json
from collections.abc import Generator
from typing import cast

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.tool import ToolInvokeMessage

def parse_invoke_response(tool_invoke_responses: Generator[AgentInvokeMessage]) -> str:
    result = ""
    for response in tool_invoke_responses:
        if response.type == ToolInvokeMessage.MessageType.TEXT:
            result += cast(ToolInvokeMessage.TextMessage, response.message).text
        elif response.type == ToolInvokeMessage.MessageType.LINK:
            result += (
                f"result link: {cast(ToolInvokeMessage.TextMessage, response.message).text}."
                + " please tell user to check it."
            )
        elif response.type in {
            ToolInvokeMessage.MessageType.IMAGE_LINK,
            ToolInvokeMessage.MessageType.IMAGE,
        }:
            result += (
                "image has been created and sent to user already, "
                + "you do not need to create it, just tell the user to check it now."
            )
        elif response.type == ToolInvokeMessage.MessageType.JSON:
            text = json.dumps(cast(ToolInvokeMessage.JsonMessage, response.message).json_object, ensure_ascii=False)
            result += f"tool response: {text}."
        else:
            result += f"tool response: {response.message!r}."
    return result
</code>

#### ログ

エージェントの思考プロセスを表示するために、通常のメッセージの戻り値に加えて、専用のインターフェースを使用して、エージェントの思考プロセス全体をツリー構造で表示できます。

##### ログの作成
- このインターフェースは、ログツリー内のノードを表すAgentLogMessageを作成して返します。
- 親が渡された場合、このノードに親ノードがあることを示します。
- デフォルトのステータスは「Success」です。ただし、タスク実行プロセスをより適切に表示したい場合は、最初にステータスを「start」に設定して「進行中」のログを表示し、タスク完了後にログステータスを「Success」に更新できます。これにより、ユーザーは最初から最後までプロセス全体を明確に把握できます。
- ラベルは、ユーザーに表示されるログタイトルとして使用されます。

<code>
def create_log_message(
    self,
    label: str,
    data: Mapping[str, Any],
    status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
    parent: AgentInvokeMessage | None = None,
) -> AgentInvokeMessage
</code>

##### ログの完了
以前に初期ステータスとして「start」を設定した場合、ログ完了エンドポイントを使用してステータスを変更できます。

<code>
def finish_log_message(
    self,
    log: AgentInvokeMessage,
    status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
    error: Optional[str] = None,
) -> AgentInvokeMessage
</code>

##### 実装例
この例では、簡単な2段階の実行プロセスを示します。最初に「考え中」の状態のログを出力し、次に実際のタスク処理を完了します。

<code>
class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        thinking_log = self.create_log_message(
            data={"Query": parameters.get("query")},
            label="Thinking",
            status=AgentInvokeMessage.LogMessage.LogStatus.START,
        )

        yield thinking_log

        llm_response = self.session.model.llm.invoke(
            model_config=LLMModelConfig(
                provider="openai",
                model="gpt-4o-mini",
                mode="chat",
                completion_params={},
            ),
            prompt_messages=[
                SystemPromptMessage(content="you are a helpful assistant"),
                UserPromptMessage(content=parameters.get("query")),
            ],
            stream=False,
            tools=[],
        )

        thinking_log = self.finish_log_message(log=thinking_log)
        yield thinking_log
        yield self.create_text_message(text=llm_response.message.content)
</code>

## モデル
### モデル設計規則
- モデルプロバイダーのルールは、Provider エンティティに基づいています。
- モデルルールは、AIModelEntity エンティティに基づいています。

以下のすべてのエンティティは Pydantic BaseModel をベースにしており、entities モジュール内で対応するエンティティを見つけることができます。

#### Provider（プロバイダ）
- provider (string) プロバイダー識別子。例：openai
- label (object) プロバイダーの表示名。多言語対応で、英語（en_US）と中国語（zh_Hans）の2言語を設定できます。
    -- zh_Hans (string) [optional] 中国語のラベル名。zh_Hans が設定されていない場合は、デフォルトで en_US が使用されます。
    -- en_US (string) 英語のラベル名
- description (object) [optional] プロバイダーの説明。多言語対応。
    -- zh_Hans (string) [optional] 中国語の説明
    -- en_US (string) 英語の説明
- icon_small (string) [optional] プロバイダーの小さなアイコン。対応するプロバイダーの実装ディレクトリ下の _assets ディレクトリに保存されます。英語と中国語の扱い方は label と同様です。
    -- zh_Hans (string) [optional] 中国語のアイコン
    -- en_US (string) 英語のアイコン
- icon_large (string) [optional] プロバイダーの大きなアイコン。対応するプロバイダーの実装ディレクトリ下の _assets ディレクトリに保存されます。英語と中国語の扱い方は label と同様です。
    -- zh_Hans (string) [optional] 中国語のアイコン
    -- en_US (string) 英語のアイコン
- background (string) [optional] 背景色のカラーコード。例：#FFFFFF。値が設定されていない場合は、フロントエンドのデフォルト色が使用されます。
- help (object) [optional] ヘルプ情報
    -- title (object) ヘルプタイトル。多言語対応。
        --- zh_Hans (string) [optional] 中国語のタイトル
        --- en_US (string) 英語のタイトル
    -- url (object) ヘルプリンク。多言語対応。
        --- zh_Hans (string) [optional] 中国語のリンク
        --- en_US (string) 英語のリンク
- supported_model_types (array[ModelType]) サポートされているモデルタイプ
- configurate_methods (array[ConfigurateMethod]) 設定方法
- provider_credential_schema ([ProviderCredentialSchema]) プロバイダーの認証情報スキーマ（プロバイダーの資格情報仕様）
- model_credential_schema ([ModelCredentialSchema]) モデルの認証情報スキーマ（モデルの資格情報仕様）

#### AIModelEntity（AIモデルエンティティ）
- model (string) モデル識別子。例：gpt-3.5-turbo
- label (object) [optional] モデルの表示名。多言語対応で、英語（en_US）と中国語（zh_Hans）の2言語を設定できます。
    -- zh_Hans (string) [optional] 中国語のラベル名
    -- en_US (string) 英語のラベル名
- model_type ([ModelType](#ModelType)) モデルタイプ
- features (array[[ModelFeature](#ModelFeature)]) [optional] サポートされている機能リスト
- model_properties (object) モデルのプロパティ
    -- mode ([LLMMode](#LLMMode)) モード（モデルタイプ llm で利用可能）
    -- context_size (int) コンテキストサイズ（モデルタイプ llm、text-embedding で利用可能）
    -- max_chunks (int) 最大チャンク数（モデルタイプ text-embedding、moderation で利用可能）
    -- file_upload_limit (int) ファイルの最大アップロード制限（単位：MB）。（モデルタイプ speech2text で利用可能）
    -- supported_file_extensions (string) サポートされているファイル拡張子形式。例：mp3、mp4（モデルタイプ speech2text の場合）
    -- default_voice (string) デフォルトのボイス。必須：alloy,echo,fable,onyx,nova,shimmer（モデルタイプ tts で利用可能）
    -- voices (list) 選択可能なボイスリスト。
        --- mode (string) ボイスモデル。（モデルタイプ tts で利用可能）
        --- name (string) ボイスモデルの表示名。（モデルタイプ tts で利用可能）
        --- language (string) ボイスモデルがサポートする言語。（モデルタイプ tts で利用可能）
    -- word_limit (int) 1回の変換における文字数制限。デフォルトでは段落ごとに区切られます。（モデルタイプ tts で利用可能）
    -- audio_type (string) サポートされているオーディオファイルの拡張子形式。例：mp3、wav（モデルタイプ tts で利用可能）
    -- max_workers (int) テキストからオーディオへの変換をサポートする同時実行タスク数。（モデルタイプ tts で利用可能）
    -- max_characters_per_chunk (int) 1チャンクあたりの最大文字数（モデルタイプ moderation で利用可能）
- parameter_rules (array[ParameterRule]) [optional] モデル呼び出しパラメータのルール
- pricing ([PriceConfig]) [optional] 価格情報
- deprecated (bool) 非推奨かどうか。非推奨の場合、モデルリストには表示されなくなりますが、すでに設定済みのものは引き続き使用できます。デフォルトは False です。

#### ModelType（モデルタイプ）
- llm テキスト生成モデル
- text-embedding テキスト埋め込みモデル
- rerank Rerank モデル
- speech2text 音声テキスト変換
- tts テキスト音声変換
- moderation 審査

#### ConfigurateMethod（構成方法）
- predefined-model 既定モデル
ユーザーは、統一されたプロバイダーの認証情報を設定するだけで、プロバイダーの既定モデルを利用できます。

- customizable-model カスタムモデル
ユーザーは、各モデルの認証情報設定を個別に追加する必要があります。

- fetch-from-remote リモートから取得
predefined-model の設定方法と同様に、統一されたプロバイダーの認証情報を設定するだけで済みます。モデルは認証情報を通じてプロバイダーから取得されます。

#### ModelFeature（モデル機能）
- agent-thought エージェントの推論。通常、70B を超えるモデルには思考連鎖能力があります。
- vision ビジョン、つまり画像理解。
- tool-call ツール呼び出し
- multi-tool-call 複数ツール呼び出し
- stream-tool-call ストリームツール呼び出し

#### FetchFrom（入手先）
- predefined-model 既定モデル
- fetch-from-remote リモートモデル

#### LLMMode（LLMモード）
- completion テキスト補完
- chat 対話

#### ParameterRule（パラメータールール）
- name (string) モデルを呼び出す際の実際のパラメータ名
- use_template (string) [optional] テンプレートを使用

デフォルトでは、5つの変数設定テンプレートが用意されています。
- temperature
- top_p
- frequency_penalty
- presence_penalty
- max_tokens

use_template でテンプレート変数名を直接設定すると、entities.defaults.PARAMETER_RULE_TEMPLATE のデフォルト設定が使用され、name と use_template 以外のすべてのパラメータを設定する必要はありません。追加の設定パラメータを設定した場合、デフォルト設定が上書きされます。openai/llm/gpt-3.5-turbo.yaml を参照してください。

- label (object) [optional] ラベル。多言語対応。
    -- zh_Hans (string) [optional] 中国語のラベル名
    -- en_US (string) 英語のラベル名
- type (string) [optional] パラメータのタイプ
    -- int 整数
    -- float 浮動小数点数
    -- string 文字列
    -- boolean ブール型
- help (string) [optional] ヘルプ情報
    -- zh_Hans (string) [optional] 中国語のヘルプ情報
    -- en_US (string) 英語のヘルプ情報
- required (bool) 必須かどうか。デフォルトは False です。
- default (int/float/string/bool) [optional] デフォルト値
- min (int/float) [optional] 最小値。数値型のみ適用。
- max (int/float) [optional] 最大値。数値型のみ適用。
- precision (int) [optional] 精度。小数点以下の桁数。数値型のみ適用。
- options (array[string]) [optional] ドロップダウンの選択肢。type が string の場合にのみ適用。設定しない、または null の場合は選択肢を制限しません。

#### PriceConfig（価格設定）
- input (float) 入力単価。つまり、Prompt の単価。
- output (float) 出力単価。つまり、返される内容の単価。
- unit (float) 価格単位。例：1M トークン単位で価格設定する場合、単価に対応するトークン数は 0.000001 になります。
- currency (string) 通貨単位

#### ProviderCredentialSchema（プロバイダー資格情報スキーマ）
- credential_form_schemas (array[CredentialFormSchema]) 資格情報フォームの仕様

#### ModelCredentialSchema（モデル認証情報スキーマ）
- model (object) モデル識別子。変数名はデフォルトで model です。
    -- label (object) モデルフォーム項目の表示名
        --- en_US (string) 英語
        --- zh_Hans (string) [optional] 中国語
    -- placeholder (object) モデルのプレースホルダー
        --- en_US (string) 英語
        --- zh_Hans (string) [optional] 中国語
- credential_form_schemas (array[CredentialFormSchema]) 資格情報フォームの仕様

#### CredentialFormSchema（資格情報フォームスキーマ）
- variable (string) フォーム項目の変数名
- label (object) フォーム項目のラベル名
    -- en_US (string) 英語
    -- zh_Hans (string) [optional] 中国語
- type ([FormType](#FormType)) フォーム項目のタイプ
- required (bool) 必須かどうか
- default (string) デフォルト値
- options (array[FormOption]) フォーム項目が select または radio の場合の専用属性。ドロップダウンの内容を定義します。
- placeholder (object) フォーム項目が text-input の場合の専用属性。フォーム項目のプレースホルダー。
    -- en_US (string) 英語
    -- zh_Hans (string) [optional] 中国語
- max_length (int) フォーム項目が text-input の場合の専用属性。入力の最大長を定義します。0 は制限なし。
- show_on (array[FormShowOnObject]) 他のフォーム項目の値が条件を満たす場合に表示します。空の場合は常に表示します。

#### FormType（フォームタイプ）
- text-input テキスト入力コンポーネント
- secret-input パスワード入力コンポーネント
- select 単一選択ドロップダウン
- radio ラジオコンポーネント
- switch スイッチコンポーネント。true と false のみをサポート。

#### FormOption（フォームオプション）
- label (object) ラベル
    -- en_US (string) 英語
    -- zh_Hans (string) [optional] 中国語
- value (string) ドロップダウンの選択肢の値
- show_on (array[FormShowOnObject]) 他のフォーム項目の値が条件を満たす場合に表示します。空の場合は常に表示します。

#### FormShowOnObject（フォーム表示オブジェクト）
- variable (string) 他のフォーム項目の変数名
- value (string) 他のフォーム項目の値

### モデルスキーマ
ここでは、プロバイダーと各モデルタイプが実装する必要があるインターフェースメソッドとパラメータについて説明します。

#### モデルプロバイダー
__base.model_provider.ModelProvider 基底クラスを継承し、以下のインターフェースを実装します。

<code>
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
</code>

- credentials (object): 認証情報

認証情報のパラメータは、サプライヤーの YAML 設定ファイルの provider_credential_schemaで定義され、api_keyなどが渡されます。検証に失敗した場合は、errors.validate.CredentialsValidateFailedErrorエラーを発生させてください。注: プリ定義モデルはこのインターフェースを完全に実装する必要があります。カスタムモデルサプライヤーは、以下のような簡単な実装で十分です。

<code>
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
</code>

#### モデル
モデルは5つの異なるモデルタイプに分類され、異なるモデルタイプは異なる基底クラスを継承し、実装する必要があるメソッドも異なります。

##### 共通インターフェース
すべてのモデルは、以下の2つのメソッドを共通して実装する必要があります。

- モデル認証情報の検証

サプライヤーの認証情報検証と同様に、ここでは個々のモデルに対して検証を行います。

<code>
def validate_credentials(self, model: str, credentials: dict) -> None:
    """
    Validate model credentials

    :param model: model name
    :param credentials: model credentials
    :return:
    """
</code>

パラメータ:
- model (string): モデル名
- credentials (object): 認証情報

認証情報のパラメータは、サプライヤーの YAML 設定ファイルのprovider_credential_schemaまたはmodel_credential_schemaで定義され、api_keyなどが渡されます。検証に失敗した場合は、errors.validate.CredentialsValidateFailedErrorエラーを発生させてください。

- 呼び出しエラーのマッピング

モデルの呼び出し中に例外が発生した場合、Dify が異なるエラーに対して適切な後続処理を実行できるように、Runtime で定義されたInvokeErrorタイプにマッピングする必要があります。Runtime Errors:

- InvokeConnectionError: 呼び出し接続エラー
- InvokeServerUnavailableError: 呼び出しサービスが利用不可
- InvokeRateLimitError: 呼び出しがレート制限に達した
- InvokeAuthorizationError: 呼び出し認証失敗
- InvokeBadRequestError: 呼び出しパラメータエラー

<code>
@property
def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
    """
    Map model invoke error to unified error
    The key is the error type thrown to the caller
    The value is the error type thrown by the model,
    which needs to be converted into a unified error type for the caller.

    :return: Invoke error mapping
    """
</code>

対応するエラーを直接発生させ、以下のように定義することもできます。これにより、後続の呼び出しでInvokeConnectionErrorなどの例外を直接発生させることができます。

#### LLM
__base.large_language_model.LargeLanguageModel 基底クラスを継承し、以下のインターフェースを実装します：

- LLM呼び出し
LLMを呼び出すためのコアメソッドを実装します。ストリーミングと同期の両方の戻り値をサポートします。

<code>
def _invoke(self, model: str, credentials: dict,
            prompt_messages: list[PromptMessage], model_parameters: dict,
            tools: Optional[list[PromptMessageTool]] = None, stop: Optional[list[str]] = None,
            stream: bool = True, user: Optional[str] = None) \
        -> Union[LLMResult, Generator]:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param prompt_messages: prompt messages
    :param model_parameters: model parameters
    :param tools: tools for tool calling
    :param stop: stop words
    :param stream: is stream response
    :param user: unique user id
    :return: full response or stream response chunk generator result
    """
</code>

- パラメータ：
    -- model (string) モデル名
    -- credentials (object) クレデンシャル

クレデンシャルのパラメータは、ベンダーのYAML構成ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。

    - prompt_messages (array[PromptMessage]) プロンプト一覧
モデルが Completion タイプの場合、リストにはUserPromptMessage 要素を1つだけ渡します。モデルが Chat タイプの場合、メッセージに応じてSystemPromptMessage、UserPromptMessage、AssistantPromptMessage、ToolPromptMessage 要素のリストを渡す必要があります。
    - model_parameters (object) モデルパラメータ。モデルパラメータは、モデルのYAML構成の parameter_rules で定義されます。
    - tools (array[PromptMessageTool]) [optional] ツール一覧。function calling における function と同等です。つまり、ツール呼び出しのためのツール一覧を渡します。
    - stop (array[string]) [optional] 停止シーケンス。モデルの出力は、停止シーケンスで定義された文字列の手前で停止します。
    - stream (bool) ストリーミング出力かどうか。デフォルトは True です。ストリーミング出力は Generator[LLMResultChunk] を返し、非ストリーミング出力は LLMResult を返します。
    - user (string) [optional] ユーザーの一意の識別子。ベンダーが不正行為を監視および検出するのに役立ちます。

- 戻り値
ストリーミング出力は Generator[LLMResultChunk] を返し、非ストリーミング出力は LLMResult を返します。

- 入力トークンの事前計算
モデルがトークン数の事前計算インターフェースを提供していない場合は、直接0を返します。

<code>
def get_num_tokens(self, model: str, credentials: dict, prompt_messages: list[PromptMessage],
                   tools: Optional[list[PromptMessageTool]] = None) -> int:
    """
    Get number of tokens for given prompt messages

    :param model: model name
    :param credentials: model credentials
    :param prompt_messages: prompt messages
    :param tools: tools for tool calling
    :return:
    """
</code>
パラメータの説明は上記の「LLM呼び出し」を参照してください。このインターフェースは、対応する model に応じて適切な tokenizer を選択して計算する必要があります。対応するモデルが tokenizer を提供していない場合は、AIModel 基底クラスの _get_num_tokens_by_gpt2(text: str) メソッドを使用して計算できます。

- カスタマイズ可能なモデルスキーマの取得 [オプション]

<code>
def get_customizable_model_schema(self, model: str, credentials: dict) -> Optional[AIModelEntity]:
    """
    Get customizable model schema

    :param model: model name
    :param credentials: model credentials
    :return: model schema
    """
</code>

ベンダーがカスタムLLMの追加をサポートしている場合、このメソッドを実装してカスタムモデルがモデルスキーマを取得できるようにできます。デフォルトでは None を返します。

OpenAI ベンダーのほとんどのファインチューニングモデルでは、ファインチューニングモデルの名前（例：gpt-3.5-turbo-1106）からその基底クラスモデルを取得し、基底クラスモデルの事前定義されたパラメータルールを返すことができます。具体的な実装については、OpenAI を参照してください。

#### TextEmbedding
__base.text_embedding_model.TextEmbeddingModel 基底クラスを継承し、以下のインターフェースを実装します。

- Embedding呼び出し
<code>
def _invoke(self, model: str, credentials: dict,
            texts: list[str], user: Optional[str] = None) \
        -> TextEmbeddingResult:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param texts: texts to embed
    :param user: unique user id
    :return: embeddings result
    """
</code>

- パラメータ：
    - model (string) モデル名
    - credentials (object) クレデンシャル

クレデンシャルのパラメータは、ベンダーのYAML構成ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。

    - texts (array[string]) テキスト一覧。バッチ処理が可能です。
    - user (string) [optional] ユーザーの一意の識別子。
ベンダーが不正行為を監視および検出するのに役立ちます。

- 戻り値：
TextEmbeddingResult エンティティ。

- トークンの事前計算

<code>
def get_num_tokens(self, model: str, credentials: dict, texts: list[str]) -> int:
    """
    Get number of tokens for given prompt messages

    :param model: model name
    :param credentials: model credentials
    :param texts: texts to embed
    :return:
    """
</code>

パラメータの説明は上記の「Embedding呼び出し」を参照してください。

上記の LargeLanguageModel と同様に、このインターフェースは対応する model に応じて適切な tokenizer を選択して計算する必要があります。対応するモデルが tokenizer を提供していない場合は、AIModel 基底クラスの _get_num_tokens_by_gpt2(text: str) メソッドを使用して計算できます。

#### Rerank
__base.rerank_model.RerankModel 基底クラスを継承し、以下のインターフェースを実装します。

- rerank呼び出し

<code>
def _invoke(self, model: str, credentials: dict,
            query: str, docs: list[str], score_threshold: Optional[float] = None, top_n: Optional[int] = None,
            user: Optional[str] = None) \
        -> RerankResult:
    """
    Invoke rerank model

    :param model: model name
    :param credentials: model credentials
    :param query: search query
    :param docs: docs for reranking
    :param score_threshold: score threshold
    :param top_n: top n
    :param user: unique user id
    :return: rerank result
    """
</code>
- パラメータ：
    - model (string) モデル名
    - credentials (object) クレデンシャル
クレデンシャルのパラメータは、ベンダーのYAML構成ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。
    - query (string) 検索クエリ
    - docs (array[string]) 並べ替え対象のテキストリスト
    - score_threshold (float) [optional] スコア閾値
    - top_n (int) [optional] 上位n件のテキストを取得
    - user (string) [optional] ユーザーの一意の識別子
ベンダーが不正行為を監視および検出するのに役立ちます。

- 戻り値：
RerankResult エンティティ。

#### Speech2text(音声テキスト変換)
__base.speech2text_model.Speech2TextModel 基底クラスを継承

- Invoke呼び出し
<code>
def _invoke(self, model: str, credentials: dict,
            file: IO[bytes], user: Optional[str] = None) \
        -> str:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param file: audio file
    :param user: unique user id
    :return: text for given audio file
    """        
</code>

- パラメータ：
    - model (string) モデル名
    - credentials (object) クレデンシャル
クレデンシャルのパラメータは、ベンダーのYAML構成ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。
    - file (File) ファイルストリーム
    - user (string) [optional] ユーザーの一意の識別子
ベンダーが不正行為を監視および検出するのに役立ちます。

- 戻り値：
音声変換された文字列。


#### Text2speech (テキスト音声変換)
__base.text2speech_model.Text2SpeechModel を継承し、以下のインターフェースを実装します。

- Invoke (呼び出し)
<code>
def _invoke(self, model: str, credentials: dict, content_text: str, streaming: bool, user: Optional[str] = None):
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param content_text: text content to be translated
    :param streaming: output is streaming
    :param user: unique user id
    :return: translated audio file
    """        
</code>

- パラメータ：
    -model (string): モデル名
    -credentials (object): 認証情報
認証情報のパラメータは、ベンダーの YAML 設定ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。
    - content_text (string): 変換するテキストコンテンツ
    -streaming (bool): ストリーミング出力を行うかどうか
    - user (string) [オプション]: ユーザーの一意な識別子
ベンダーが不正利用を監視・検出するのに役立ちます。

- 戻り値：
テキスト変換後の音声ストリーム。

#### Moderation (モデレーション)
__base.moderation_model.ModerationModel を継承し、以下のインターフェースを実装します。
- Invoke (呼び出し)
<code>
def _invoke(self, model: str, credentials: dict,
            text: str, user: Optional[str] = None) \
        -> bool:
    """
    Invoke large language model

    :param model: model name
    :param credentials: model credentials
    :param text: text to moderate
    :param user: unique user id
    :return: false if text is safe, true otherwise
    """
</code>
- パラメータ：
    - model (string): モデル名
    - credentials (object): 認証情報
認証情報のパラメータは、ベンダーの YAML 設定ファイルの provider_credential_schema または model_credential_schema で定義され、api_key などが渡されます。
    - text (string): テキストコンテンツ
    -user (string) [オプション]: ユーザーの一意な識別子

ベンダーが不正利用を監視・検出するのに役立ちます。

- 戻り値：
入力テキストが安全な場合は False、そうでない場合は True を返します。

#### Entity(エンティティ)
##### PromptMessageRole (プロンプトメッセージの役割)
メッセージの役割を定義する列挙型です。
<code>
class PromptMessageRole(Enum):
    """
    Enum class for prompt message.
    """
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
</code>

##### PromptMessageContentType (プロンプトメッセージのコンテンツタイプ)
メッセージコンテンツのタイプを定義する列挙型です。テキストと画像の2種類があります。

<code>
class PromptMessageContentType(Enum):
    """
    Enum class for prompt message content type.
    """
    TEXT = 'text'
    IMAGE = 'image'
</code>

##### PromptMessageContent (プロンプトメッセージのコンテンツ)
メッセージコンテンツの基底クラスです。パラメータ定義のみに用いられ、直接の初期化はできません。

<code>
class PromptMessageContent(BaseModel):
    """
    Model class for prompt message content.
    """
    type: PromptMessageContentType
    data: str  # コンテンツデータ
</code>

現在、テキストと画像の2種類のタイプがサポートされており、テキストと複数の画像を同時に渡すことができます。それぞれ TextPromptMessageContent および ImagePromptMessageContent を初期化して渡す必要があります。

##### TextPromptMessageContent

<code>
class TextPromptMessageContent(PromptMessageContent):
    """
    テキストプロンプトメッセージのコンテンツを定義するモデルクラスです。
    """
    type: PromptMessageContentType = PromptMessageContentType.TEXT
</code>

テキストと画像を同時に送信する場合、テキストはこのエンティティを content リストの一部として構成する必要があります。

##### ImagePromptMessageContent

<code>
class ImagePromptMessageContent(PromptMessageContent):
    """
    Model class for image prompt message content.
    """
    class DETAIL(Enum):
        LOW = 'low'
        HIGH = 'high'

    type: PromptMessageContentType = PromptMessageContentType.IMAGE
    detail: DETAIL = DETAIL.LOW  # 解像度
</code>
画像とテキストを同時に送信する場合、画像はこのエンティティを content リストの一部として構成する必要があります。
data には、画像の url または base64 エンコードされた文字列を指定できます。

##### PromptMessage
すべての Role メッセージの基底クラスで、パラメータ定義のみに使用され、インスタンス化はできません。

<code>
class PromptMessage(ABC, BaseModel):
    """
    Model class for prompt message.
    """
    role: PromptMessageRole  # メッセージの役割
    content: Optional[str | list[PromptMessageContent]] = None  # 文字列またはコンテンツリストのいずれかを指定できます。コンテンツリストはマルチモーダルに対応するためのもので、詳細は PromptMessageContent の説明を参照してください。
    name: Optional[str] = None  # 名前（オプション）
</code>

##### UserPromptMessage
ユーザーメッセージを表す UserMessage のメッセージボディです。

<code>
class UserPromptMessage(PromptMessage):
    """
    Model class for user prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.USER
</code>

##### AssistantPromptMessage
モデルからの応答メッセージを表し、通常は few-shots やチャット履歴の入力に使用されます。

<code>
class AssistantPromptMessage(PromptMessage):
    """
    Model class for assistant prompt message.
    """
    class ToolCall(BaseModel):
        """
        Model class for assistant prompt message tool call.
        """
        class ToolCallFunction(BaseModel):
            """
            Model class for assistant prompt message tool call function.
            """
            name: str  # ツールの名前
            arguments: str  # ツールの引数

        id: str  # ツールID。OpenAI のツール呼び出しでのみ有効で、ツール呼び出しの一意なIDです。同じツールを複数回呼び出すことができます。
        type: str  # デフォルトは function
        function: ToolCallFunction  # ツール呼び出し情報

    role: PromptMessageRole = PromptMessageRole.ASSISTANT
    tool_calls: list[ToolCall] = []  # モデルが応答したツール呼び出しの結果です（tools が渡され、モデルがツールを呼び出す必要があると判断した場合のみ返されます）。
</code>

tool_calls は、モデルに tools が渡された後、モデルから返されるツール呼び出しのリストです。

##### SystemPromptMessage
システムメッセージを表し、通常はモデルにシステム命令を設定するために使用されます。

<code>
class SystemPromptMessage(PromptMessage):
    """
    Model class for system prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.SYSTEM
</code>

##### ToolPromptMessage
ツールメッセージを表し、ツールの実行結果をモデルに渡して、次の計画を立てるために使用されます。

<code>
class ToolPromptMessage(PromptMessage):
    """
    Model class for tool prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.TOOL
    tool_call_id: str  # ツール呼び出しID。OpenAI のツール呼び出しをサポートしない場合は、ツール名を渡すこともできます。
</code>

基底クラスの content にはツールの実行結果を渡します。

#### PromptMessageTool
<code>
class PromptMessageTool(BaseModel):
    """
    Model class for prompt message tool.
    """
    name: str  # ツール名
    description: str  # ツールの説明
    parameters: dict  # ツールパラメータ（辞書形式）
<code>

##### LLMResult
<code>
class LLMResult(BaseModel):
    """
    Model class for llm result.
    """
    model: str  # 使用モデル
    prompt_messages: list[PromptMessage]  # プロンプトメッセージリスト
    message: AssistantPromptMessage  # 返信メッセージ
    usage: LLMUsage  # トークン及び費用情報
    system_fingerprint: Optional[str] = None  # リクエスト指紋（OpenAIの定義に準拠）

</code>

##### LLMResultChunkDelta
ストリーミング結果の各イテレーションにおける差分エンティティ

<code>
class LLMResultChunkDelta(BaseModel):
    """
    Model class for llm result chunk delta.
    """
    index: int  # 順番
    message: AssistantPromptMessage  # 返信メッセージ
    usage: Optional[LLMUsage] = None  # トークン及び費用情報（最後のチャンクのみ）
    finish_reason: Optional[str] = None  # 終了理由（最後のチャンクのみ）
</code>

##### LLMResultChunk
ストリーミング結果の各イテレーションエンティティ

<code>
class LLMResultChunk(BaseModel):
    """
    Model class for llm result chunk.
    """
    model: str  # 使用モデル
    prompt_messages: list[PromptMessage]  # プロンプトメッセージリスト
    system_fingerprint: Optional[str] = None  # リクエスト指紋（OpenAIの定義に準拠）
    delta: LLMResultChunkDelta  # 各イテレーションで変化する内容
</code>

##### LLMUsage

<code>
class LLMUsage(ModelUsage):
    """
    Model class for llm usage.
    """
    prompt_tokens: int  # プロンプト使用トークン数
    prompt_unit_price: Decimal  # プロンプト単価
    prompt_price_unit: Decimal  # プロンプト価格単位（単価が適用されるトークン数）
    prompt_price: Decimal  # プロンプト料金
    completion_tokens: int  # 回答使用トークン数
    completion_unit_price: Decimal  # 回答単価
    completion_price_unit: Decimal  # 回答価格単位（単価が適用されるトークン数）
    completion_price: Decimal  # 回答料金
    total_tokens: int  # 総使用トークン数
    total_price: Decimal  # 総料金
    currency: str  # 通貨単位
    latency: float  # リクエスト処理時間（秒）
</code>

##### TextEmbeddingResult
<code>
class TextEmbeddingResult(BaseModel):
    """
    Model class for text embedding result.
    """
    model: str  # 使用モデル
    embeddings: list[list[float]]  # 埋め込みベクトルリスト（テキストに対応）
    usage: EmbeddingUsage  # 使用情報
</code>

##### EmbeddingUsage
<code>
class EmbeddingUsage(ModelUsage):
    """
    Model class for embedding usage.
    """
    tokens: int  # 使用トークン数
    total_tokens: int  # 総使用トークン数
    unit_price: Decimal  # 単価
    price_unit: Decimal  # 価格単位（単価が適用されるトークン数）
    total_price: Decimal  # 総料金
    currency: str  # 通貨単位
    latency: float  # リクエスト処理時間（秒）
</code>

##### RerankResult
<code>
class RerankResult(BaseModel):
    """
    Model class for rerank result.
    """
    model: str  # 使用モデル
    docs: list[RerankDocument]  # リランク後のドキュメントリスト
</code>

##### RerankDocument
<code>
class RerankDocument(BaseModel):
    """
    Model class for rerank document.
    """
    index: int  # 元の順番
    text: str  # ドキュメントテキスト
    score: float  # スコア
</code>


## 一般的な標準使用
本文では、プラグイン開発における共通構造について簡単に説明します。

### パス仕様
マニフェストまたは任意のyamlファイルでファイルパスを指定する場合、ファイルタイプに基づいて以下の2つのルールに従ってください：

- 画像や動画などのマルチメディアファイル（例：プラグインのicon）の場合、プラグインのルートディレクトリの下の_assetsフォルダに配置します。
- .pyや.yamlなどの通常のテキストファイルの場合、プラグインプロジェクト内の絶対パスを使用します。

### 共通構造
プラグインを定義する際、ツール、モデル、インターフェース間で共有できるデータ構造があります。以下がこれらの共有構造です。

### I18nObject
I18nObjectは、IETF BCP 47標準に準拠した国際化構造で、現在4つの言語をサポートしています：

- en_US
- zh_Hans
- ja_Jp
- pt_BR

### ProviderConfig
ProviderConfigは、ToolとEndpointの両方に適用可能な共通プロバイダーフォーム構造です。
- name (string): フォーム項目名
- label (I18nObject, 必須): IETF BCP 47に準拠
- type (provider_config_type, 必須): フォームタイプ
- scope (provider_config_scope): オプション範囲、typeにより異なる
- required (bool): 空にできない
- default (any): デフォルト値、基本タイプfloat int stringのみサポート
- options (list[provider_config_option]): オプション、typeがselectの場合のみ使用
- helper (object): ヘルプドキュメントリンクラベル、IETF BCP 47に準拠
- url (string): ヘルプドキュメントリンク
- placeholder (object): IETF BCP 47に準拠

### ProviderConfigOption(object)
- value(string, 必須)：値
- label(object, 必須)：IETF BCP 47に準拠

### ProviderConfigType(string)
- secret-input (string)：設定情報が暗号化される
- text-input(string)：プレーンテキスト
- select(string)：ドロップダウンボックス
- boolean(bool)：スイッチ
- model-selector(object)：プロバイダー名、モデル名、モデルパラメータなどを含むモデル設定情報
- app-selector(object)：アプリID
- tool-selector(object)：ツールプロバイダー、名前、パラメータなどを含むツール設定情報
- dataset-selector(string)：TBD

### ProviderConfigScope(string)
- typeがmodel-selectorの場合
    -- all
    -- llm
    -- text-embedding
    -- rerank
    -- tts
    -- speech2text
    -- moderation
    -- vision
- typeがapp-selectorの場合
    -- all
    -- chat
    -- workflow
    -- completion
- typeがtool-selectorの場合
    -- all
    -- plugin
    -- api
    -- workflow

### ModelConfig
- provider (string): プラグインIDを含むプロバイダー名、形式はlanggenius/openai/openai
- model (string): 具体的なモデル名
- model_type (enum): モデルタイプの列挙、このドキュメントを参照

### NodeResponse
- inputs (dict): ノードに最終的に入力される変数
- outputs (dict): ノード出力結果
- process_data (dict): ノード実行中に生成されたデータ

### ToolSelector
- provider_id (string): ツールプロバイダー名
- tool_name (string): ツール名
- tool_description (string): ツールの説明
- tool_configuration (dict[str, Any]): ツール設定情報
- tool_parameters (dict[str, dict]): LLM推論が必要なパラメータ
    -- name (string): パラメータ名
    -- type (string): パラメータタイプ
    -- required (bool): 必須かどうか
    -- description (string): パラメータの説明
    -- default (any): デフォルト値
    -- options (list[string]): 利用可能なオプション


## 永続化されたストレージ
プラグイン内のToolとEndpointを個別に見ると、ほとんどの場合、単一のラウンドの対話、つまりリクエストを送信してデータを返し、タスクが終了するだけであることがわかります。

長期的なデータの保存が必要な場合、例えば永続的なメモリを実装する場合、プラグインには永続的なストレージ機能が必要です。永続ストレージメカニズムにより、プラグインは同じWorkspace内でデータを永続的に保存する機能を持つことができます。現在はKVデータベースを提供してストレージのニーズを満たしており、将来的には実際の使用状況に基づいて、より柔軟で強力なストレージインターフェースを導入する可能性があります。

### ストレージキー
#### エントリーポイント
<code>
self.session.storage
</code>

#### エンドポイント
<code>
def set(self, key: str, val: bytes) -> None:
    pass
</code>
bytesが渡されることに注意してください。これにより、実際にファイルを保存することができます。

### キーの取得
#### エントリーポイント
<code>
self.session.storage
</code>

#### エンドポイント
<code>
def get(self, key: str) -> bytes:
    pass
</code>

### キーの削除
#### エントリーポイント
<code>
self.session.storage
</code>

#### エンドポイント
</code>
def delete(self, key: str) -> None:
    pass
</code>

## Difyサービスの逆呼び出し

プラグインは、Difyメインプラットフォーム内の特定のサービスを自由に呼び出し、プラグインの機能を拡張できます。

呼び出し可能なDifyモジュール
- App:プラグインは、Difyプラットフォーム内のAppデータにアクセスできます。
- Model:プラグインは、Difyプラットフォーム内のLLM機能をバックコールできます。これには、プラットフォーム内のすべてのモデルタイプと機能（TTS、Rerankなど）が含まれます。
- Tool:プラグインは、Difyプラットフォーム内の他のツールタイプのプラグインを呼び出すことができます。
- Node:プラグインは、Difyプラットフォーム内の特定のChatflow/Workflowアプリケーション内のノードを呼び出すことができます。

### App（アプリ）

リバース呼び出しとは、プラグインがDify内のAppデータにアクセスできることを意味します。このモジュールは、ストリーミングと非ストリーミングの両方のAppコールをサポートしています。

#### エンドポイントタイプ：
- Chatbot/Agent/Chatflowタイプのアプリケーションは、すべてチャットタイプのアプリケーションであり、同じ入力パラメータと出力パラメータを持つため、統一的にチャットインターフェースとして扱うことができます。
- Workflowアプリケーションは、独立したワークフローインターフェースを占有します。
- Completion（テキスト生成）アプリケーションは、独立したCompletionエンドポイントを占有します。

注意：プラグインは、プラグインと同じWorkspace内のAppにのみアクセスできます。

#### チャットインターフェースのリクエスト エントリーポイント
##### エントリーポイント
<code>
self.session.app.chat
</code>

##### エンドポイント仕様
<code>
def invoke(
    self,
    app_id: str,
    inputs: dict,
    response_mode: Literal["streaming", "blocking"],
    conversation_id: str,
    files: list,
) -> Generator[dict, None, None] | dict:
    pass
</code>

response_modeがstreamingの場合、インターフェースはGenerator[dict]を返し、それ以外の場合はdictを返します。具体的なインターフェースフィールドについては、ServiceApiの戻り値を参照してください。

##### 例
Endpoint内でチャットタイプのAppをリクエストし、結果を直接返すことができます：

<code>
import json
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class Duck(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        与えられたリクエストでエンドポイントを呼び出します。
        """
        app_id = values["app_id"]
        def generator():
            response = self.session.app.workflow.invoke(
                app_id=app_id, inputs={}, response_mode="streaming", files=[]
            )
            for data in response:
                yield f"{json.dumps(data)} <br>"
        return Response(generator(), status=200, content_type="text/html")
</code>

####ワークフローエンドポイント エントリーポイント

##### エントリー
<code>
self.session.app.workflow
</code>

##### エンドポイント仕様
<code>
def invoke(
    self,
    app_id: str,
    inputs: dict,
    response_mode: Literal["streaming", "blocking"],
    files: list,
) -> Generator[dict, None, None] | dict:
    pass
</code>

#### Completionエンドポイントのリクエスト
##### エントリー
<code>
self.session.app.completion
</code>

##### エンドポイント仕様
<code>
def invoke(
    self,
    app_id: str,
    inputs: dict,
    response_mode: Literal["streaming", "blocking"],
    files: list,
) -> Generator[dict, None, None] | dict:
    pass
</code>

### Model（モデル）
リバースモデルリクエストとは、プラグインがDify内のLLM機能に対してリバースリクエストを行う能力を指し、TTS、Rerankなど、プラットフォーム上のすべてのモデルタイプと機能が含まれます。

モデルのリクエストには、ModelConfigタイプのパラメータを渡す必要があることに注意してください。その構造は共通仕様定義で参照でき、この構造は異なるタイプのモデルで若干の違いがあります。

例えば、LLMタイプのモデルの場合、completion_paramsとmodeパラメータを含める必要があります。この構造は手動で構築するか、model-selectorタイプのパラメータまたは設定を使用することができます。

#### LLMのリクエスト
##### エントリー
<code>
self.session.model.llm
</code>

##### エンドポイント：
<code>
def invoke(
    self,
    model_config: LLMModelConfig,
    prompt_messages: list[PromptMessage],
    tools: list[PromptMessageTool] | None = None,
    stop: list[str] | None = None,
    stream: bool = True,
) -> Generator[LLMResultChunk, None, None] | LLMResult:
    pass
</code>

注意：リクエストするモデルにtool_call機能がない場合、ここで渡されるツールは効果を持ちません。

##### 例
ツールでOpenAIのgpt-4o-miniモデルをリクエストする場合は、以下のサンプルコードを参照してください：
<code>
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.message import SystemPromptMessage, UserPromptMessage

class LLMTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        response = self.session.model.llm.invoke(
            model_config=LLMModelConfig(
                provider='openai',
                model='gpt-4o-mini',
                mode='chat',
                completion_params={}
            ),
            prompt_messages=[
                SystemPromptMessage(
                    content='you are a helpful assistant'
                ),
                UserPromptMessage(
                    content=tool_parameters.get('query')
                )
            ],
            stream=True
        )

        for chunk in response:
            if chunk.delta.message:
                assert isinstance(chunk.delta.message.content, str)
                yield self.create_text_message(text=chunk.delta.message.content)
</code>
コードではtool_parametersからqueryパラメータが渡されていることに注意してください。

#### ベストプラクティス
LLMModelConfigを手動で構築することは推奨されません。代わりに、UIでユーザーが希望のモデルを選択できるようにします。この場合、以下の設定に従ってmodelパラメータを追加することでツールのパラメータリストを変更できます：

<code>
identity:
  name: llm
  author: Dify
  label:
    en_US: LLM
    zh_Hans: LLM
    pt_BR: LLM
description:
  human:
    en_US: A tool for invoking a large language model
    zh_Hans: 用于调用大型语言模型的工具
    pt_BR: A tool for invoking a large language model
  llm: A tool for invoking a large language model
parameters:
  - name: prompt
    type: string
    required: true
    label:
      en_US: Prompt string
      zh_Hans: 提示字符串
      pt_BR: Prompt string
    human_description:
      en_US: used for searching
      zh_Hans: 用于搜索网页内容
      pt_BR: used for searching
    llm_description: key words for searching
    form: llm
  - name: model
    type: model-selector
    scope: llm
    required: true
    label:
      en_US: Model
      zh_Hans: 使用的模型
      pt_BR: Model
    human_description:
      en_US: Model
      zh_Hans: 使用的模型
      pt_BR: Model
    llm_description: which Model to invoke
    form: form
extra:
  python:
    source: tools/llm.py
</code>

この例では、モデルのスコープがllmとして指定されているため、ユーザーはllmタイプのパラメータのみを選択できることに注意してください。これにより、上記の例のコードを以下のように変更できます：

<code>
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.message import SystemPromptMessage, UserPromptMessage

class LLMTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        response = self.session.model.llm.invoke(
            model_config=tool_parameters.get('model'),
            prompt_messages=[
                SystemPromptMessage(
                    content='you are a helpful assistant'
                ),
                UserPromptMessage(
                    content=tool_parameters.get('query')
                )
            ],
            stream=True
        )

        for chunk in response:
            if chunk.delta.message:
                assert isinstance(chunk.delta.message.content, str)
                yield self.create_text_message(text=chunk.delta.message.content)
</code>

#### 要約のリクエスト
このエンドポイントを使用してテキストを要約することができます。現在のワークスペースのシステムモデルを使用してテキストを要約します。

##### エントリー：
<code>
self.session.model.summary
</code>

##### エンドポイント：
- text: 要約するテキスト
- instruction: 追加の指示。要約のスタイルをカスタマイズできます

<code>
def invoke(
    self, text: str, instruction: str,
) -> str:
</code>

#### テキスト埋め込みのリクエスト
##### エントリー
<code>
self.session.model.text_embedding
</code>

##### エンドポイント
<code>
def invoke(
    self, model_config: TextEmbeddingResult, texts: list[str]
) -> TextEmbeddingResult:
    pass
</code>

#### Rerankのリクエスト
##### エントリー
<code>
self.session.model.rerank
</code>

##### エンドポイント
<code>
def invoke(
    self, model_config: RerankModelConfig, docs: list[str], query: str
) -> RerankResult:
    pass
</code>

#### TTSのリクエスト
##### エントリー
<code>
self.session.model.tts
</code>

##### エンドポイント
<code>
def invoke(
    self, model_config: TTSModelConfig, content_text: str
) -> Generator[bytes, None, None]:
    pass
</code>

注意：TTSエンドポイントが返すバイトストリームはmp3オーディオバイトストリームで、各イテレーションで完全なオーディオを返します。より高度な処理タスクを実行したい場合は、適切なライブラリを選択してください。

#### 音声認識のリクエスト
##### エントリー：
<code>
self.session.model.speech2text
</code>

##### エンドポイント：
<code>
def invoke(
    self, model_config: Speech2TextModelConfig, file: IO[bytes]
) -> str:
    pass
</code>

ここで、fileはmp3エンコードされたオーディオファイルです。

#### モデレーションのリクエスト
##### エントリー：
<code>
self.session.model.moderation
</code>

##### エンドポイント：
<code>
def invoke(self, model_config: ModerationModelConfig, text: str) -> bool:
    pass
</code>

このエンドポイントがtrueを返す場合、textに機密コンテンツが含まれていることを示します。


### Tool（ツール）
以下のようなシナリオに遭遇した場合：
- ツールタイププラグインが機能を実装したが、期待を満たしておらずデータの再処理が必要な場合
- タスクがWebクローリングを必要とし、クローリングサービスの選択に柔軟性が必要な場合
- 複数のツールの戻り値を組み合わせる必要があるが、Workflowアプリケーションでの処理が困難な場合

これらの場合、プラグイン内の他の実装済みツールをリクエストする必要があります。これらのツールは、マーケットプレイスのツールプラグイン、自作のWorkflow as Tool、またはカスタムツールである可能性があります。

上記の要件は、プラグインのself.session.toolフィールドを使用することで達成できます。

#### インストール済みツールのリクエスト
プラグインが現在のWorkspaceにインストールされている様々なツール（他のツールタイププラグインを含む）をリクエストすることができます。

##### エントリー：
<code>
self.session.tool
</code>

##### エンドポイント：
<code>
def invoke_builtin_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
</code>

ここで、providerはプラグインIDとツールプロバイダー名を組み合わせたもので、langgenius/google/googleのような形式です。tool_nameは具体的なツール名、parametersはそのツールに渡すパラメータです。

#### Workflow as Toolのリクエスト
Workflow as Toolの詳細については、このドキュメントを参照してください。
##### エントリー：
<code>
self.session.tool
</code>

##### エンドポイント：
<code>
def invoke_workflow_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
</code>

ここで、providerはツールのID、tool_nameはツール作成時に必要となります。

#### カスタムツールのリクエスト
##### エントリー：
<code>
self.session.tool
</code>

##### エンドポイント：
<code>
def invoke_api_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
</code>

ここで、providerはツールのID、tool_nameはOpenAPIのoperation_idです。存在しない場合は、Difyによって自動生成されたtool_nameで、ツール管理ページで確認できます。

### Node（ノード）
リバースノードリクエストとは、プラグインがDifyのChatflow/Workflowアプリケーション内の特定のノードにアクセスする能力を指します。

WorkflowのParameterExtractorとQuestionClassifierノードは、複雑なPromptとコードロジックをカプセル化しており、LLMを通じたハードコーディングでは解決が困難な多くのタスクを実行できます。プラグインはこれら2つのノードをリクエストすることができます。

#### パラメータ抽出ノードのリクエスト
##### エントリー
<code>
self.session.workflow_node.parameter_extractor
</code>

##### エンドポイント
<code>
def invoke(
    self,
    parameters: list[ParameterConfig],
    model: ModelConfig,
    query: str,
    instruction: str = "",
) -> NodeResponse
    pass
</code>

ここで、parametersは抽出するパラメータのリスト、modelはLLMModelConfig仕様に従い、queryはパラメータ抽出のソーステキスト、instructionはLLMへの追加指示を含み、NodeResponse構造はドキュメントで参照できます。

##### 例
会話から人の名前を抽出したい場合は、以下のコードを参照してください：

<code>
from collections.abc import Generator
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool
from dify_plugin.entities.workflow_node import ModelConfig, ParameterConfig

class ParameterExtractorTool(Tool):
    def _invoke(
        self, tool_parameters: dict
    ) -> Generator[ToolInvokeMessage, None, None]:
        response = self.session.workflow_node.parameter_extractor.invoke(
            parameters=[
                ParameterConfig(
                    name="name",
                    description="name of the person",
                    required=True,
                    type="string",
                )
            ],
            model=ModelConfig(
                provider="langgenius/openai/openai",
                name="gpt-4o-mini",
                completion_params={},
            ),
            query="My name is John Doe",
            instruction="Extract the name of the person",
        )
        yield self.create_text_message(response.outputs["name"])
</code>

#### 質問分類ノードのリクエスト
##### エントリー
<code>
self.session.workflow_node.question_classifier
</code>

##### エンドポイント
<code>
def invoke(
    self,
    classes: list[ClassConfig],
    model: ModelConfig,
    query: str,
    instruction: str = "",
) -> NodeResponse:
    pass
</code>

このエンドポイントのパラメータはParameterExtractorと一致しており、最終結果はNodeResponse.outputs['class_name']に格納されます。