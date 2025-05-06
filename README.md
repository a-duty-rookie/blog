# Zenn記事管理リポジトリ

このリポジトリは、Zenn記事の管理のためのリポジトリです。

---

## 👣 公開記事一覧

<!-- BEGIN_PUB_TABLE -->
| internal_key   | article_num   | article_sum_num   | title   | category   | status   | zenn_url   | memo   |
|----------------|---------------|-------------------|---------|------------|----------|------------|--------|
<!-- END_PUB_TABLE -->

---

## 👣 ネタ一覧

<!-- BEGIN_SEEDS_TABLE -->
| internal_key   | article_num   | article_sum_num   | title   | category   | status   | zenn_url   | memo   |
|----------------|---------------|-------------------|---------|------------|----------|------------|--------|
<!-- END_SEEDS_TABLE -->

---

## 👀 ステータス定義

| ステータス | 説明                                                 |
| ---------- | ---------------------------------------------------- |
| ネタ       | アイデア段階。とりあえず書きたいことだけメモした状態 |
| 構成中     | セクション構成や内容整理を始めた段階                 |
| 草稿中     | 本文を書き始めている状態                             |
| 公開済     | Zennに記事として公開した状態                         |

---

## ✨ データ管理フロー

Googleフォームからネタを登録し、Googleスプレッドシートに蓄積、さらにGitHub ActionsによりCSVへ同期され、ここ（README）に自動反映される仕組みになっています。

```plaintext
Google Form → Google Spreadsheet → (GitHub Actions) → mst_zenn_ideas.csv → README.md
```

* `scripts/sync_spreadsheet_to_csv.py` により、スプレシートの新規レコードがCSVに追加されます
* `mst_zenn_ideas.csv` をもとに `scripts/sync_csv_to_md.py` によってMarkdown テーブルが生成され、README.md に自動挿入されます
* 定期実行は GitHub Actions のcron設定により1時間ごとに動作します

---

## 👤 作成者

* GitHub : [a-duty-rookie](https://github.com/a-duty-rookie)
* Zenn : [a\_duty\_rookie](https://zenn.dev/a_duty_rookie)
* X : [a\_duty\_rookie](https://x.com/a_duty_rookie)
* Tableau Public : [こちら](https://public.tableau.com/app/profile/taro.yu/vizzes)
