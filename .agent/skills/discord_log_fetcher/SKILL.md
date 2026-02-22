---
name: discord_log_fetcher
description: DiscordChatExporter を使って Discord チャンネルのログを読み取り専用で取得するための手順と自動化コマンド集。
---

# Discord Log Fetcher Skill

DiscordChatExporter CLI を使い、Discord チャンネルのメッセージ履歴を**読み取り専用**で取得する。
書き込み・送信は一切行わない。Bot トークンまたはユーザートークンの両方に対応。

## Core Directives
- **Read-Only 厳守**: メッセージの送信・削除・編集を行う API は呼ばない。
- **トークン秘匿**: トークンは環境変数 `DISCORD_TOKEN` に格納し、コマンドライン引数に直書きしない。
- **形式選択**: 用途に応じた出力形式を選ぶ（下記「形式早見表」参照）。
- **日付範囲指定**: 大量取得の場合は `--after` / `--before` で期間を絞る。

## 形式早見表

| 用途 | 推奨形式 | オプション |
|------|----------|-----------|
| データ解析・パース | JSON | `--format Json` |
| 人間が読む | HTML (Dark) | `--format HtmlDark` |
| テキスト検索 | TXT | `--format PlainText` |
| スプレッドシート | CSV | `--format Csv` |

## Setup

### 1. DiscordChatExporter CLI のインストール
```bash
# .NET 8 が必要
dotnet tool install -g DiscordChatExporter.Cli
```

または GitHub Releases から単体バイナリをダウンロード:
[https://github.com/Tyrrrz/DiscordChatExporter/releases](https://github.com/Tyrrrz/DiscordChatExporter/releases)

### 2. トークンの環境変数登録
```bash
export DISCORD_TOKEN="your_token_here"
```

### 3. Bot トークンを使う場合の前提
- Discord Developer Portal で `Message Content Intent` を **ON** にする。
- トークンプレフィックスに `-b` (Bot) フラグを付ける。

## コマンド集（典型的なユースケース）

### 単一チャンネルを全量 JSON で取得
```bash
discordchatexporter-cli export \
  -t "$DISCORD_TOKEN" \
  -c CHANNEL_ID \
  --format Json \
  -o ./logs/
```

### Bot トークンで取得（`-b` フラグ追加）
```bash
discordchatexporter-cli export \
  -t "$DISCORD_TOKEN" -b \
  -c CHANNEL_ID \
  --format Json \
  -o ./logs/
```

### 期間を絞って取得（2025 年以降）
```bash
discordchatexporter-cli export \
  -t "$DISCORD_TOKEN" \
  -c CHANNEL_ID \
  --after "2025-01-01" \
  --format Json \
  -o ./logs/
```

### サーバー（ギルド）内の全チャンネルを一括取得
```bash
discordchatexporter-cli exportguild \
  -t "$DISCORD_TOKEN" \
  -g GUILD_ID \
  --format Json \
  -o ./logs/
```

### チャンネル ID の確認方法
```bash
# チャンネル一覧の表示（サーバー ID 指定）
discordchatexporter-cli channels -t "$DISCORD_TOKEN" -g GUILD_ID
```

## Workflow

1. **Identify**: `channels` コマンドでターゲットの CHANNEL_ID を確認する。
2. **Filter**: `--after` / `--before` で期間を絞る（省略すると全量）。
3. **Export**: `--format Json` で取得し `./logs/` に保存する。
4. **Verify**: 取得ファイルの行数・日付範囲を確認する。
   ```bash
   wc -l ./logs/*.json
   ```
5. **Parse**: JSON の場合は `jq` で必要フィールドだけ抽出する。
   ```bash
   jq '.messages[] | {timestamp, author: .author.name, content}' ./logs/*.json
   ```

## 注意事項
- **セルフボット禁止**: ユーザートークンを用いた自動化は Discord ToS違反リスクあり。公式 Bot API を優先する。
- **レートリミット**: CLI は自動的にレートリミットを処理するが、大量取得時は時間がかかる。
- **スレッド**: スレッドのログも取得する場合、各スレッドに個別の CHANNEL_ID が必要。
- **添付ファイル**: `--media` フラグを追加するとメディアファイルもローカルダウンロードされる。
