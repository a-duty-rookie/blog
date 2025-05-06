from pathlib import Path

import pandas as pd  # type:ignore

# --- 設定 ---

MST_CSV_PATH = Path("mst_zenn_ideas.csv")

# --- 公開済みステータスの記事のurlを自動生成

df = pd.read_csv(MST_CSV_PATH)

for raw in df.iterrows():
    raw = raw[1]
    main_num = str(raw.article_num)
    sub_num = str(raw.article_sub_num)
    url_text = (
        "[記事を見る]"
        f"(https://zenn.dev/a_duty_rookie/articles/article_{main_num:0>5}_{sub_num})"
    )
    if raw.status == "公開済":
        df.loc[
            (df.internal_key == raw.internal_key)
            & (df.article_num == raw.article_num)
            & (df.article_sub_num == raw.article_sub_num),
            "zenn_url",
        ] = url_text

df.to_csv(MST_CSV_PATH, index=False)
