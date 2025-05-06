import re
from pathlib import Path

import pandas as pd  # type:ignore

# --- 設定 ---
README_PATH = Path("README.md")
MST_CSV_PATH = Path("mst_zenn_ideas.csv")

status_dict = {
    "ネタ": 1,
    "構成中": 2,
    "草稿中": 3,
    "公開済": 4,
    "削除済": 5,
}

# --- マスタを読み込んで仕分け
df = pd.read_csv(MST_CSV_PATH)
df["status_id"] = df.status.apply(
    lambda s: status_dict[s] if s in status_dict.keys() else 0
)
df = df.fillna("")
df = df.sort_values(["status_id", "article_num", "article_sum_num", "internal_key"])

pub_df = df.loc[df.status_id == 4].drop("status_id", axis=1)
seeds_df = df.loc[df.status_id.between(1, 3, "both")].drop("status_id", axis=1)

# --- markdownに挿入
md_txt = README_PATH.read_text()
for df, symbol in zip([pub_df, seeds_df], ["PUB", "SEEDS"]):
    md_tbl = df.to_markdown(index=False)  # tabulateインストール必須
    md_txt = re.sub(
        pattern=f"<!-- BEGIN_{symbol}_TABLE -->.*<!-- END_{symbol}_TABLE -->",
        repl=(
            f"<!-- BEGIN_{symbol}_TABLE -->\n"
            + md_tbl
            + f"\n<!-- END_{symbol}_TABLE -->"
        ),
        string=md_txt,
        flags=re.DOTALL,
    )

README_PATH.write_text(md_txt, encoding="utf-8")
