# Zenn記事管理リポジトリ

このリポジトリは、Zenn記事の管理のためのリポジトリです。

---

## 👣 公開記事一覧

<!-- BEGIN_PUB_TABLE -->
| title                       | zenn_url                                                                   |
|:----------------------------|:---------------------------------------------------------------------------|
| はじめに                    | [article_00001_1](https://zenn.dev/a_duty_rookie/articles/article_00001_1) |
| 一致性と不偏性①             | [article_00002_1](https://zenn.dev/a_duty_rookie/articles/article_00002_1) |
| 一致性と不偏性②             | [article_00002_2](https://zenn.dev/a_duty_rookie/articles/article_00002_2) |
| 一致性と不偏性③             | [article_00002_3](https://zenn.dev/a_duty_rookie/articles/article_00002_3) |
| 最小二乗法と仲良くなりたい① | [article_00003_1](https://zenn.dev/a_duty_rookie/articles/article_00003_1) |
| 最小二乗法と仲良くなりたい② | [article_00003_2](https://zenn.dev/a_duty_rookie/articles/article_00003_2) |
| 最小二乗法と仲良くなりたい③ | [article_00003_3](https://zenn.dev/a_duty_rookie/articles/article_00003_3) |
<!-- END_PUB_TABLE -->

---

## 👣 ネタ一覧

<!-- BEGIN_SEEDS_TABLE -->
| title   | status   |
|---------|----------|
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
